from collections import defaultdict
from intcode import print_grid


def find_accessible(grid, pos, keys):
    directions = [1, 2, 3, 4]
    DX = {1: 1, 2: -1, 3: 0, 4: 0}
    DY = {1: 0, 2: 0, 3: 1, 4: -1}
    accessible = {}
    to_check = [(pos, 0)]
    checked = []
    while to_check:
        (cur, length) = to_check.pop()
        checked.append(cur)
        for i in directions:
            test_pos = (cur[0] + DX[i], cur[1] + DY[i])
            if test_pos == pos or test_pos in checked:
                continue
            if test_pos in grid and grid[test_pos] in ['.', '@']:
                to_check.append((test_pos, length + 1))
            elif test_pos in grid and grid[test_pos] in 'abcdefghijklmnopqrstuvwxyz' and grid[test_pos] not in keys:
                accessible[test_pos] = (grid[test_pos], length + 1)
                pos = test_pos
                print('adding {} as accessible with val {}'.format(test_pos, accessible[test_pos]))
            elif test_pos in grid and grid[test_pos] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if grid[test_pos].lower() in keys:
                    to_check.append((test_pos, length + 1))
    return accessible

def run(filename):
    grid = {}
    all_keys = []
    with open(filename) as f:
        start_pos = None
        lines = [x.strip() for x in f.readlines()]
        x = y = 0
        for l in lines:
            x = 0
            for c in l:
                if c == '@':
                    start_pos = (x, y)
                elif c in 'abcdefghijklmnopqrstuvwxyz':
                    all_keys.append(c)
                grid[(x, y)] = c
                x += 1
            y += 1
    print_grid(grid, None)

    print('starting at ', start_pos)

    paths = defaultdict(list)
    pos = start_pos
    keys = []
    path = []
    accessible = find_accessible(grid, pos, keys)
    potential_moves = list(accessible.keys())
    moves = 0
    while potential_moves:
        move = potential_moves.pop()
        print('moving to ', move)
        key = accessible[move]
        print('got key ', key)
        path.append(key[0])
        moves += key[1]
        if len(path) == len(all_keys):
            paths[moves] = path.copy()
            path.pop()
            moves -= key[1]

        print('finding accessible from ', move)
        accessible = find_accessible(grid, move, path)
        print(accessible)
        potential_moves.extend(list(accessible.keys()))
        # accessible = find_accessible(grid, pos, keys)
        # print(accessible)
        # min_cost = min(x[1] for x in accessible.values())
        # min_accessible = [p for p in accessible.keys() if accessible[p][1] == min_cost]
        # key = accessible[min_accessible[0]][0]
        # path.append(key)
        # grid[min_accessible[0]] = '.'
        # moves += min_cost
        # print('added {} to moves to get {} while getting key {}'.format(min_cost, moves, key))
        # pos = min_accessible[0]
    print(paths)

run('18.test')
run('18.test.2')
