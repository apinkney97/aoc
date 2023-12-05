from __future__ import annotations

from abc import ABC, abstractmethod

from aoc import utils

# EXAMPLE = True
EXAMPLE = False

# this is a bit nasty, but avoids needing to add leading zeros
HEX_TO_BYTES = {
    "0": (0, 0, 0, 0),
    "1": (0, 0, 0, 1),
    "2": (0, 0, 1, 0),
    "3": (0, 0, 1, 1),
    "4": (0, 1, 0, 0),
    "5": (0, 1, 0, 1),
    "6": (0, 1, 1, 0),
    "7": (0, 1, 1, 1),
    "8": (1, 0, 0, 0),
    "9": (1, 0, 0, 1),
    "A": (1, 0, 1, 0),
    "B": (1, 0, 1, 1),
    "C": (1, 1, 0, 0),
    "D": (1, 1, 0, 1),
    "E": (1, 1, 1, 0),
    "F": (1, 1, 1, 1),
}


def load_data():
    data = utils.load_data(2021, 16, example=EXAMPLE)

    bits = []

    for c in data[0]:
        bits.extend(HEX_TO_BYTES[c.upper()])

    return bits


def bits_to_int(bits: list[int]) -> int:
    return int(bits_to_str(bits), 2)


def bits_to_str(bits: list[int]) -> str:
    return "".join(str(b) for b in bits)


class Packet(ABC):
    def __init__(self, version: int, type_: int, bits_consumed: int):
        self._version = version
        self._type = type_
        self._bits_consumed = bits_consumed

    @abstractmethod
    def serialize(self) -> str:
        return f"{self._version:03b}{self._type:03b}"

    @abstractmethod
    def version_sum(self) -> int:
        pass

    @property
    @abstractmethod
    def value(self) -> int:
        pass

    @staticmethod
    def deserialize(bits: list[int]) -> Packet:
        type_ = Packet.parse_type(bits)

        if type_ == 4:
            return Literal.deserialize(bits)

        return Operator.deserialize(bits)

    @staticmethod
    def parse_version(bits: list[int]):
        return bits_to_int(bits[0:3])

    @staticmethod
    def parse_type(bits: list[int]):
        return bits_to_int(bits[3:6])

    def bit_length_out(self):
        return len(self.serialize())

    def bits_consumed(self):
        return self._bits_consumed


# Every Packet has VVV TTT (Version, Type)

# Type 4: Literal value
#  followed by multiple groups of HNNNN where H is 1 for initial groups, 0 for last group, NNNN
# ie VVV TTT [1NNNN]* 0NNNN


class Literal(Packet):
    TYPE = 4

    def __init__(self, version: int, value: int, bits_consumed: int):
        super().__init__(version, type_=self.TYPE, bits_consumed=bits_consumed)
        self._value = value

    @property
    def value(self) -> int:
        return self._value

    def version_sum(self) -> int:
        return self._version

    def serialize(self) -> str:
        value_str = f"{self._value:b}"
        value_str = "0" * ((4 - (len(value_str) % 4)) % 4) + value_str

        groups = []
        num_groups = len(value_str) // 4
        for i in range(num_groups):
            header_bit = 1 if i < num_groups - 1 else 0
            nybble = value_str[i * 4 : (i + 1) * 4]
            groups.append(f"{header_bit}{nybble}")

        data = "".join(groups)
        return super().serialize() + data

    @staticmethod
    def deserialize(bits: list[int]) -> Literal:
        version = Packet.parse_version(bits)
        header_bit = 1

        offset = 6
        value_bits = []
        while header_bit:
            header_bit = bits[offset]
            value_bits.extend(bits[offset + 1 : offset + 5])
            offset += 5

        return Literal(version, value=bits_to_int(value_bits), bits_consumed=offset)


class Operator(Packet):
    def __init__(
        self,
        version: int,
        type_: int,
        bits_consumed: int,
        sub_packets: list[Packet],
    ):
        super().__init__(version=version, type_=type_, bits_consumed=bits_consumed)
        self._sub_packets: list[Packet] = sub_packets

    def serialize(self) -> str:
        raise NotImplementedError("TODO")

    def version_sum(self) -> int:
        return self._version + sum(p.version_sum() for p in self._sub_packets)

    @staticmethod
    def deserialize(bits: list[int]) -> Packet:
        # Operators contain one or more packets.
        # Operators have a `length type Id`
        # VVV TTT I
        # I=0 is followed by 15 bit number (total length in bits of sub-packets)
        # I=1 is followed by 11 bit number (number of sub-packets immediately contained)

        version = Packet.parse_version(bits)
        type_ = Packet.parse_type(bits)
        length_type_id = bits[6]

        sub_packets = []

        bits_consumed = 7

        if length_type_id == 0:
            number_width = 15
            bits_consumed += number_width
            sub_packets_bit_length = bits_to_int(bits[7 : 7 + number_width])
            sub_consumed = 0
            while sub_consumed < sub_packets_bit_length:
                sub_bits = bits[bits_consumed + sub_consumed :]
                sub_packet = Packet.deserialize(sub_bits)
                sub_packets.append(sub_packet)
                sub_consumed += sub_packet.bits_consumed()

            bits_consumed += sub_packets_bit_length

        else:
            number_width = 11
            sub_packets_count = bits_to_int(bits[7 : 7 + number_width])
            bits_consumed += number_width
            for _ in range(sub_packets_count):
                sub_packet = Packet.deserialize(bits[bits_consumed:])
                sub_packets.append(sub_packet)
                bits_consumed += sub_packet.bits_consumed()
        return Operator(version, type_, bits_consumed, sub_packets)

    @property
    def value(self) -> int:
        sps = self._sub_packets
        match self._type:
            case 0:
                return sum(p.value for p in sps)
            case 1:
                return utils.product(p.value for p in sps)
            case 2:
                return min(p.value for p in sps)
            case 3:
                return max(p.value for p in sps)
            case 5:
                return 1 if sps[0].value > sps[1].value else 0
            case 6:
                return 1 if sps[0].value < sps[1].value else 0
            case 7:
                return 1 if sps[0].value == sps[1].value else 0


DATA = load_data()


def part1() -> int:
    packet = Packet.deserialize(DATA)
    return packet.version_sum()


def part2() -> int:
    packet = Packet.deserialize(DATA)
    return packet.value


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
