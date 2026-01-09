from enum import StrEnum, auto
from typing import TypeVar

T = TypeVar('T')
GridRow = list[T]
Grid = list[GridRow]

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


def get_value(grid_row: GridRow, col: int, direction: Direction) -> T:
    return ''

def set_value(grid_row: GridRow, row: int, direction: Direction, val: str) -> T:
    return ''

def splits[T](grid: list[list[T]]) -> int:
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
