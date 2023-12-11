# Advent of code

Repository of submissions to [Advent of Code](https://adventofcode.com/) (by year)

## Table of Contents

- [Usage](#usage)
- [License](#license)

## Usage

**`python>=3.8+`**
* stdin terminates on empties
* will execute 2nd solution if applicable

```bash
python <YYYY>/dayDD_<puzzlename>.py < stdin
```

## Skel

- template

```python
import sys

def solver(line):
    ...

def main():
    nums = []
    while line:=sys.stdin.readline().strip():
        nums.append(solver(line))
    print(sum(nums))

if __name__ == "__main__":
    main()
```
## License

This project is licensed under the [MIT License](LICENSE).
