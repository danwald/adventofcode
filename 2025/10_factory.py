from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Indicator:
    mask: int

    @classmethod
    def from_str(cls, data: str) -> "Indicator":
        mask = 0
        for idx, ch in enumerate(data[1:-1]):
            if ch != ".":
                mask |= 1 << idx
        return cls(mask)


@dataclass(slots=True, frozen=True)
class Button:
    mask: list[int]

    @classmethod
    def from_str(cls, data: list[str]) -> "Button":
        tups = []
        for tup in data:
            mask = 0
            buttons = eval(tup)
            if isinstance(buttons, int):
                mask |= 1 << buttons
            else:
                for button in buttons:
                    mask |= 1 << button
            tups.append(mask)
        return cls(tups)


@dataclass(slots=True, frozen=True)
class Joltage:
    joltage: list[int]

    @classmethod
    def from_str(cls, data: str) -> "Joltage":
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
                    Indicator.from_str(indicator),
                    Button.from_str(button),
                    Joltage.from_str(joltage),
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
