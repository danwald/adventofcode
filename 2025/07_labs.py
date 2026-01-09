from enum import StrEnum, auto

Grid = list[list[str]]

class Direction(StrEnum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGTH = auto()

def get_grid(data: str) -> Grid:
    acc: Grid = []
    for line in data.split():
        acc.append(list(line))
    return acc


def get_value(grid: Grid, row: int, direction: Direction) -> str:
    return ''

def splits(grid: list[list[str]]) -> int:
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            match grid[row][col]:
                case '.':
                    pass
                case 'S':
                    grid[row][col] = '|'
                case '^':
                    pass
                case: '|':
                    pass




def main(data: str, **_) -> int:
    grid = get_grid(data)
    return splits(grid)


if __name__ == "__main__":
    assert (
        main(
            """
.......S.......
.......^.......
...............
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""
        )
        == 21
    )
