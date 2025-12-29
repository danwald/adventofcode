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
    # print(content.ranges)
    return content


def is_fresh(ranges: list[tuple[int, int]], ing: int) -> bool:
    l, r = 0, len(ranges) - 1
    while l <= r:
        m = (r + l) // 2
        lo, hi = ranges[m]
        # print("\t", l, m, r, lo, hi, ing)
        if lo <= ing <= hi:
            # print(ing)
            return True
        if ing < lo:
            r = m - 1
        elif ing > hi:
            l = m + 1
    return False


def main(data, **_) -> int:
    content = get_content(data)
    # print(content.ranges)
    fresh = 0
    for ing in content.ingredients:
        if is_fresh(content.ranges, ing):
            fresh += 1
    print(fresh)
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
