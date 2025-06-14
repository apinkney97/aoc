import typing


class Command(typing.NamedTuple):
    command: str
    output: list[str]


type Data = list[Command]


class BaseFile:
    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def size(self) -> int:
        raise NotImplementedError


class File(BaseFile):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self._size = size

    @property
    def size(self) -> int:
        return self._size


class Dir(BaseFile):
    def __init__(self, name: str, contents: list[BaseFile] | None = None):
        super().__init__(name)
        self._contents = contents or []

    @property
    def size(self) -> int:
        return sum(child.size for child in self._contents)

    def append(self, file: BaseFile) -> None:
        self._contents.append(file)


def parse_data(data: list[str]) -> Data:
    commands = []

    command = ""
    output: list[str] = []

    for line in data:
        if line.startswith("$ "):
            if command:
                commands.append(Command(command, output))
            command = line[2:]
            output = []
        else:
            output.append(line)

    if command:
        commands.append(Command(command, output))

    return commands


def to_path(cwd: list[str]) -> str:
    return "/" + "/".join(cwd)


def get_dirs(commands: list[Command]) -> dict[str, Dir]:
    cwd: list[str] = []
    dirs: dict[str, Dir] = {"/": Dir("/")}

    file: BaseFile

    for command in commands:
        if command.command == "cd /":
            cwd = []
        elif command.command == "cd ..":
            cwd.pop()
        elif command.command.startswith("cd "):
            cwd.append(command.command[3:])
        elif command.command.startswith("ls"):
            for line in command.output:
                details, name = line.split(" ", maxsplit=1)
                if details == "dir":
                    file = Dir(name)
                    dirs[to_path(cwd + [name])] = file
                else:
                    file = File(name, int(details))
                dirs[to_path(cwd)].append(file)

    return dirs


def part1(data: Data) -> int:
    dirs = get_dirs(data)

    total = 0
    for dir_ in dirs.values():
        size = dir_.size
        if size <= 100000:
            total += size

    return total


def part2(data: Data) -> int:
    available = 70000000
    need = 30000000

    dirs = get_dirs(data)
    used = dirs["/"].size
    free = available - used

    space_needed = need - free

    print(used, free, space_needed)

    best = available
    for dir_ in dirs.values():
        size = dir_.size
        if size >= space_needed:
            best = min(size, best)

    return best
