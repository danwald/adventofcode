from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Indicator:
    indicator: str

    @classmethod
    def file_str(cls, data: str) -> "Indicator":
        return cls(data[1:-1])


@dataclass(slots=True, frozen=True)
class Button:
    button: list[tuple[int, ...]]

    @classmethod
    def file_str(cls, data: list[str]) -> "Button":
        tups = []
        for tup in data:
            tups.append(eval(tup))
        return cls(tups)


@dataclass(slots=True, frozen=True)
class Joltage:
    joltage: list[int]

    @classmethod
    def file_str(cls, data: str) -> "Joltage":
        jolts = []
        for jolt in data.strip()[1:-1].split(","):
            jolts.append(int(jolt))
        return cls(jolts)


@dataclass(slots=True, frozen=True)
class Record:
    indicator: Indicator
    button: Button
    joltage: Joltage

    @classmethod
    def from_str(cls, data: str) -> "list[Record]":
        records = []
        for line in data.strip().split("\n"):
            indicator, *button, joltage = line.split(" ")
            records.append(
                cls(
                    Indicator.file_str(indicator),
                    Button.file_str(button),
                    Joltage.file_str(joltage),
                )
            )
        return records

    @property
    def least_presses(self) -> int:
        return 0


def main(data, **_) -> int:
    records = Record.from_str(data)
    return sum([record.least_presses for record in records])


if __name__ == "__main__":
    assert main("""
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
                """) == 7
