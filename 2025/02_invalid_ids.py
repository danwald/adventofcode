from typing import Iterator


def runner(start: int, end: int) -> Iterator[int]:
    assert start <= end
    for i in range(start, end + 1):
        yield i


def bookends(r: str) -> tuple[int, int]:
    # print(r)
    start, end = [int(val) for val in r.split("-", 2)]
    return start, end


def _get_eq_splits(num: int, max_half) -> (
    tuple[()]
    | tuple[
        int,
        ...,
    ]
):
    snum = str(num)
    if not num:
        return tuple()
    if max_half and not len(snum) % 2:
        pivot, odd_len = divmod(len(snum), 2)
        if odd_len:
            return tuple()
        return int(snum[:pivot]), int(snum[-pivot:])
    return tuple()


def is_invalid(val: int, max_half: bool) -> bool:
    splits = _get_eq_splits(val, max_half)
    if max_half:
        if not splits or splits[0] != splits[1]:
            return False
        return True
    return False


def main(*args: str, max_half=True) -> int:
    invalids, ranges = [], args[0].split(",")
    for r in ranges:
        start, end = bookends(r)
        for val in runner(start, end):
            if is_invalid(val, max_half):
                invalids.append(val)

    # print(invalids, sum(invalids))
    return sum(invalids)


if __name__ == "__main__":
    assert (
        main(
            "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
            "824824821-824824827,2121212118-2121212124,"
            "1698522-1698528,446443-446449,38593856-38593862,565653-565659",
            max_half=True,
        )
        == 1227775554
    )
    assert (
        main(
            "2157315-2351307,9277418835-9277548385,4316210399-4316270469,5108-10166,"
            "872858020-872881548,537939-575851,712-1001,326613-416466,53866-90153,907856-1011878,"
            "145-267,806649-874324,6161532344-6161720341,1-19,543444404-543597493,35316486-35418695,"
            "20-38,84775309-84908167,197736-309460,112892-187377,336-552,4789179-4964962,726183-793532,"
            "595834-656619,1838-3473,3529-5102,48-84,92914229-92940627,65847714-65945664,64090783-64286175,"
            "419838-474093,85-113,34939-52753,14849-30381",
            max_half=True,
        )
        == 29818212493
    )
