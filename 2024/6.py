import copy

from concurrent.futures import ThreadPoolExecutor
from itertools import repeat


DIRECTIONS = ['^', '>', 'v', '<']
CHANGE = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_start(m):
    for r in range(len(m)):
        row = m[r]
        idx = None
        for d in DIRECTIONS:
            if d in row:
                idx = row.index(d)
                return (r, idx, d)

def run(m):
    (row, col, d) = get_start(m)
    visited = set()
    loop = set()
    examined = set()

    prev_row = None
    prev_col = None
    (dy, dx) = CHANGE[DIRECTIONS.index(d)]
    while row >= 0 and row < len(m) and col >= 0 and col < len(m[0]):
        examined.add((row, col))
        if m[row][col] == '#':
            # hit an obstacle, back up one step and turn
            row = prev_row
            col = prev_col
            d2 = DIRECTIONS[(DIRECTIONS.index(d) + 1) % len(DIRECTIONS)]
            d = d2
        else:
            if (row, col, d) in loop:
                raise Exception('loop')
            loop.add((row, col, d))
            visited.add((row, col))
            (dy, dx) = CHANGE[DIRECTIONS.index(d)]
            prev_row = row
            prev_col = col
            row += dy
            col += dx

    return (len(visited), examined)

def test_map(m, candidate):
    (r, c) = candidate
    #print(f'Testing candidate ({r}, {c})')
    new_map = copy.deepcopy(m)
    new_map[r][c] = '#'
    try:
        run(new_map)
    except Exception as e:
        return True
    return False


if __name__ == '__main__':
    m = []
    with open('6.in') as f:
        m = [[c for c in x.strip()] for x in f.readlines()]

    (num_visited, examined) = run(m)
    print('part1:', num_visited)

    loops = []
    print(f'Map sized {len(m)} x {len(m[0])}')
    candidates = []
    for r in range(len(m)):
        for c in range(len(m[r])):
            if (r, c) in examined and m[r][c] == '.':
                candidates.append((r, c))
    print(f'{len(candidates)} candidate positions')
    with ThreadPoolExecutor(max_workers=10) as executor:
        res = list(executor.map(test_map, repeat(m), candidates))
    print('part2:', sum(res))
