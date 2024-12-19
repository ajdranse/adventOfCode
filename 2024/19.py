import copy
from functools import cache

AVAILABLE = None
DESIRED = None
PATHS = None
SEEN = {}

def solve(word):
    if word in SEEN:
        return SEEN[word]

    if word == '':
        return 1

    paths = []
    for a in AVAILABLE:
        if word.startswith(a):
            paths.append(solve(word[len(a):]))
    SEEN[word] = sum(paths)
    return sum(paths)

if __name__ == '__main__':
    with open('19.in') as f:
        inp = [x.strip() for x in f.readlines()]
    AVAILABLE = inp[0].split(', ')
    DESIRED = inp[2:]

    print(f'Have {len(DESIRED)} desired patterns')
    print(f'Have {len(AVAILABLE)} patterns')

    successful = 0
    total_paths = 0
    for i, d in enumerate(DESIRED):
        count = solve(d)
        if count > 0:
            successful += 1
            total_paths += count
    print('part1:', successful)
    print('part2:', total_paths)
