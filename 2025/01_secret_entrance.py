import sys

from collections import namedtuple

Heading = namedtuple("Heading", ["dr", "mg"])


class Dial:
    def __init__(self, teeth: int = 100):
        self.teeth = teeth
        self.pos = 0
        self._pass = 0

    def __len__(self) -> int:
        return self.teeth

    @property
    def password(self) -> int:
        return self._pass

    def _how(self, line: str) -> Heading:
        ln = line.strip()
        d, m = ln[0], ln[1:]
        return Heading(-1 if d == "L" else 1, int(m))

    def rotate(self, line: str) -> None:
        heading = self._how(line)
        rots, inc = divmod(heading.mg, len(self))
        self._pass += rots
        if heading.dr < 0:
            self.pos -= inc
            if self.pos < 0:
                self.pos = len(self) + self.pos
                self._pass += 1
        else:
            self.pos += inc
            if self.pos > len(self):
                self.pos = self.pos - len(self)
                self._pass += 1

        print(line, rots, inc, self.pos, self.password)


def main():
    dl = Dial()
    while line := sys.stdin.readline().strip():
        dl.rotate(line)
    return dl.password, dl.pos


if __name__ == "__main__":

    print(main())
