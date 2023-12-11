import sys

def get_indices(word, line):
    hits, start = [], 0
    while (idx:=line.find(word, start)) != -1:
        hits.append((idx, word, ))
        start = idx + len(word)
    return hits

def words_to_digits(line):
    w2d = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    matches = []
    for word in w2d:
        matches.extend(get_indices(word, line))
    matches.sort()
    for _, word in matches:
        line = line.replace(word, w2d[word], 1)
    return line

def get_coords(line):
    nums = [int(letter) for letter in words_to_digits(line) if letter.isdigit()]
    return int(f'{nums[0]}{nums[-1]}')

def main():
    nums = []
    while line:=sys.stdin.readline().strip():
        nums.append(get_coords(line))
        #print(f'"{line}" -> {nums[-1]}')
    print(sum(nums))

if __name__ == "__main__":
    main()
