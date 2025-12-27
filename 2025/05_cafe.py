import dataclasses


@dataclasses.dataclass
class Content:
    ranges: list[tuple[int, int]]
    ingredients: list[int]


def get_content(input: str) -> Content:
    lines = input.strip().split("\n")
    reading_ranges = True
    content = Content([], [])
    for line in lines:
        if not line:
            reading_ranges = False
            continue
        if reading_ranges:
            lo, hi = line.split("-")
            content.ranges.append((int(lo), int(hi)))
        else:
            content.ingredients.append(int(line))
    content.ranges.sort()
    return content


def is_fresh(ranges: list[tuple[int, int]], ing: int) -> bool:
    l, r = 0, len(ranges) - 1
    while l < r:
        m = (r + l) // 2
        print(l, m, r)
        lo, hi = ranges[m]
        if lo <= ing <= hi:
            return True
        if ing < lo:
            r = m
        elif ing > hi:
            l = m
    return False


def main(data, **_) -> int:
    content = get_content(data)
    fresh = 0
    for ing in content.ingredients:
        if is_fresh(content.ranges, ing):
            fresh += 1
    return fresh


if __name__ == "__main__":
    assert (
        main(
            """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
        )
        == 3
    )
