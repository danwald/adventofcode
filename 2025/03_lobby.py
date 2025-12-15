from typing import Iterator


def get_battery_bank(banks: str) -> Iterator[str]:
    for bank in banks.split(","):
        yield bank.strip()


def larger(nums: str, cur: int, oth: int) -> bool:

    return nums[cur] < nums[oth] if cur != oth else False


def get_max_jolts(bank: str) -> int:
    if not bank:
        return 0
    n = len(bank)
    ml, mr, l, r = 0, n - 1, 0, n - 1

    while l < r:
        if larger(bank, ml, l):
            ml = l
        if larger(bank, mr, r):
            mr = r
        l += 1
        r -= 1
    val = int("".join([bank[ml], bank[mr]]))
    print(f"{bank} => {val} {l, r, ml, mr}")
    return val


def main(nums: str, **_) -> int:
    jolts: list[int] = []
    for bank in get_battery_bank(nums):
        jolts.append(get_max_jolts(bank))
    return sum(jolts)


if __name__ == "__main__":
    assert (
        main("987654321111111, 811111111111119,234234234234278,818181911112111") == 357
    )
