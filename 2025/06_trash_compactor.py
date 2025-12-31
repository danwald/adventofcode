from typing import Iterator
from functools import reduce
import operator


def get_grid(data, **_) -> list[list[int | str]]:
    grid: list[list[int | str]] = []
    data = data.strip().split("\n")
    nums, ops = data[:-1], data[-1]
    for row in nums:
        grid.append([int(col) for col in row.strip().split()])
    grid.append([str(op) for op in ops.strip().split()])
    return grid


def rows(grid: list[list[int | str]]) -> Iterator[list[int | str]]:
    height, width = len(grid), len(grid[0])
    for col in range(width):
        yield [grid[row][col] for row in range(height)]


def main(data, **_) -> int:
    ops = {"*": operator.mul, "+": operator.add}
    grid = get_grid(data)
    row_ans = []
    for row in rows(grid):
        *nums, op = row
        row_ans.append(reduce(ops[op], nums))
    return sum(row_ans)


if __name__ == "__main__":
    assert (
        main(
            """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""
        )
        == 4277556
    )
