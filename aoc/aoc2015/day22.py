from __future__ import annotations

from typing import Generator, Literal, NamedTuple

from rich.pretty import pprint

from aoc import config
from aoc.utils import PQ

type Data = tuple[int, int]


class Spell(NamedTuple):
    name: str
    mana_cost: int
    damage: int
    heal: int = 0


class Effect(NamedTuple):
    name: str
    mana_cost: int
    turns: int
    armour: int = 0
    damage: int = 0
    mana: int = 0


# Spells happen immediately (ie on that turn).
# Effects first happen at the start of the next turn.

m = Spell(name="Magic Missile", mana_cost=53, damage=4)
d = Spell(name="Drain", mana_cost=73, damage=2, heal=2)
s = Effect(name="Shield", mana_cost=113, turns=6, armour=7)
p = Effect(name="Poison", mana_cost=173, turns=6, damage=3)
r = Effect(name="Recharge", mana_cost=229, turns=5, mana=101)

SPELLS: list[Spell | Effect] = [m, d, s, p, r]


def example_order() -> Generator[Spell | Effect, None, None]:
    yield r
    yield s
    yield d
    yield p
    yield m


example = example_order()


def get_spells() -> list[Spell | Effect]:
    if not config.EXAMPLE:
        return SPELLS
    return [next(example)]


class GameState(NamedTuple):
    player_hp: int
    player_mana: int

    boss_hp: int
    boss_dp: int

    player_turn_next: bool

    shield_turns: int
    poison_turns: int
    recharge_turns: int

    mana_spent: int

    @property
    def winner(self) -> Literal["BOSS"] | Literal["PLAYER"] | None:
        if self.boss_hp <= 0:
            return "PLAYER"
        if self.player_hp <= 0:
            return "BOSS"
        return None


def parse_data(data: list[str]) -> Data:
    boss_hp = int(data[0].split()[2])
    boss_dp = int(data[1].split()[1])
    return boss_hp, boss_dp


def next_moves(state: GameState, hard_mode: bool = False) -> list[GameState]:
    player_hp = state.player_hp

    if hard_mode and state.player_turn_next:
        player_hp -= 1

        if player_hp <= 0:
            return []

    # Apply effects
    shield_turns = state.shield_turns
    poison_turns = state.poison_turns
    recharge_turns = state.recharge_turns

    boss_hp = state.boss_hp
    mana = state.player_mana

    if shield_turns > 0:
        armour = 7
        shield_turns -= 1
    else:
        armour = 0

    if config.EXAMPLE:
        turn = "Player" if state.player_turn_next else "Boss"
        print(f"\n-- {turn} turn --")
        print(f"- Player has {state.player_hp} hit points, {armour} armor, {mana} mana")
        print(f"- Boss has {boss_hp} hit points")

    if poison_turns > 0:
        boss_hp -= 3
        poison_turns -= 1

    if recharge_turns > 0:
        mana += 101
        recharge_turns -= 1

    # Check if boss is dead, otherwise play
    if boss_hp <= 0:
        return [
            GameState(
                player_hp=state.player_hp,
                player_mana=mana,
                boss_hp=boss_hp,
                boss_dp=state.boss_dp,
                player_turn_next=not state.player_turn_next,
                shield_turns=shield_turns,
                poison_turns=poison_turns,
                recharge_turns=recharge_turns,
                mana_spent=state.mana_spent,
            )
        ]

    if not state.player_turn_next:
        # Boss's turn, only one child state

        return [
            GameState(
                player_hp=state.player_hp - max(1, state.boss_dp - armour),
                player_mana=mana,
                boss_hp=boss_hp,
                boss_dp=state.boss_dp,
                player_turn_next=True,
                shield_turns=shield_turns,
                poison_turns=poison_turns,
                recharge_turns=recharge_turns,
                mana_spent=state.mana_spent,
            )
        ]

    # Otherwise apply all possible moves and return all states.
    new_states = []

    for move in get_spells():
        shield_turns_ = shield_turns
        poison_turns_ = poison_turns
        recharge_turns_ = recharge_turns

        if move.mana_cost > mana:
            # Too expensive
            continue

        player_hp_ = player_hp
        boss_hp_ = boss_hp

        if isinstance(move, Spell):
            # Apply immediately
            player_hp_ += move.heal
            boss_hp_ -= move.damage

        elif isinstance(move, Effect):
            if move.damage:
                if poison_turns_ > 0:
                    continue
                poison_turns_ = move.turns

            if move.armour:
                if shield_turns_ > 0:
                    continue
                shield_turns_ = move.turns

            if move.mana:
                if recharge_turns_ > 0:
                    continue
                recharge_turns_ = move.turns

        new_states.append(
            GameState(
                player_hp=player_hp_,
                player_mana=mana - move.mana_cost,
                boss_hp=boss_hp_,
                boss_dp=state.boss_dp,
                player_turn_next=False,
                shield_turns=shield_turns_,
                poison_turns=poison_turns_,
                recharge_turns=recharge_turns_,
                mana_spent=state.mana_spent + move.mana_cost,
            )
        )

    return new_states


def part1(data: Data, hard_mode: bool = False) -> int:
    if config.EXAMPLE:
        start_state = GameState(
            player_hp=10,
            player_mana=250,
            player_turn_next=True,
            boss_hp=14,
            boss_dp=8,
            shield_turns=0,
            poison_turns=0,
            recharge_turns=0,
            mana_spent=0,
        )
    else:
        start_state = GameState(
            player_hp=50,
            player_mana=500,
            player_turn_next=True,
            boss_hp=data[0],
            boss_dp=data[1],
            shield_turns=0,
            poison_turns=0,
            recharge_turns=0,
            mana_spent=0,
        )

    pq: PQ[GameState] = PQ()
    pq.add_item(start_state, priority=start_state.mana_spent)

    while pq:
        state = pq.pop_item()
        # pprint(state)

        if state.winner:
            if state.winner == "PLAYER":
                if config.DEBUG:
                    pprint(state)
                return state.mana_spent

        else:
            for new_state in next_moves(state, hard_mode=hard_mode):
                pq.add_item(new_state, new_state.mana_spent)

    return -1


def part2(data: Data) -> int:
    return part1(data, hard_mode=True)
