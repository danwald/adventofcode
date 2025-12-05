import sys

from collections import namedtuple

Heading = namedtuple("Heading", ["dr", "dt"])


class Dial:
    def __init__(self, pos: int = 50, teeth: int = 100):
        self.teeth = teeth
        self._pass = 0
        self.pos = pos

    def __len__(self) -> int:
        return self.teeth

    @property
    def password(self) -> int:
        return self._pass

    def _how(self, line: str) -> Heading:
        ln = line.strip()
        d, m = ln[0], ln[1:]
        return Heading(-1 if d == "L" else 1, int(m))

    def rotate(self, line: str, pst=False, dbg=False) -> bool:
        heading = self._how(line)
        rots, rdt = divmod(heading.dt, len(self))
        thru = 0
        c0 = not self.pos
        self.pos += heading.dr * rdt
        if self.pos >= len(self):
            self.pos -= len(self)
            if not c0:
                thru += 1
        elif self.pos < 0:
            self.pos += len(self)
            if not c0:
                thru += 1

        if not (0 <= self.pos < len(self)):
            if dbg:
                print(f"{line}[{self.pos}] R:{rots} = {self.password}")
            return False
        if not self.pos:
            if dbg:
                print(f"{line}[{self.pos}] R:{rots} = {self.password}", end="")
            self._pass += 1
            if dbg:
                print(f"->{self.password}")

        if pst:
            if dbg:
                print(f"{line}[{self.pos}] R:{rots} = {self.password}", end="")
            self._pass += rots + thru
            if dbg:
                print(f"-> {self.password}")

        return True


def main():
    dl = Dial()
    while line := sys.stdin.readline().strip():
        if not dl.rotate(line, False):
            print(f"failed at {line}, {dl.password}")
    return dl.password, dl.pos


if __name__ == "__main__":

    print(main())
