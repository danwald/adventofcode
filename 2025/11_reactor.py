type AdjDict = dict[str, list[str]]


def get_adj_dict(lines: str) -> AdjDict:
    ret: AdjDict = {}
    for line in lines.split("\n"):
        frm, too = line.split(":", 2)
        ret[frm] = too.split()
    return ret


def get_start(ad: AdjDict, key_val: str = "you") -> str | None:
    for key, vals in ad.items():
        for val in vals:
            if key_val == val:
                return key


def get_paths(ad: AdjDict, key: str, end: str = "out") -> list[list[str]]:
    paths, search, ans = [], ad[key], []
    while search:
        cur = search.pop()
        ans.append(cur)
        for path in ad[cur]:
            if path == end:
                paths = ans[:]
                continue
            search.append(path)
        print(paths)
    return paths


def main(input: str, **_) -> int:
    ad = get_adj_dict(input)
    start_key = get_start(ad)
    assert start_key

    return len(get_paths(ad, start_key))


if __name__ == "__main__":
    assert main("""aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""") == 5
