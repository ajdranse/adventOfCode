import copy
import matplotlib.pyplot as plt

def parse():
    with open('15.in') as f:
        inp = [x.strip() for x in f.readlines()]

    m = []
    idx = 0
    while '#' in inp[idx]:
        l = inp[idx]
        m.append([c for c in l])
        idx += 1
    idx += 1

    moves = ''
    while idx < len(inp):
        l = inp[idx]
        moves += l
        idx += 1

    return(m, moves)

def check(m, dy, dx, mover, level=0):
    m = copy.deepcopy(m)
    indent = ' ' * level
    next_y = mover[0] + dy
    next_x = mover[1] + dx
    next_pos = m[next_y][next_x]
    if next_pos == '#':
        # wall
        return (False, m)
    elif next_pos in ['O', '[', ']']:
        # barrel or parts of barrel
        moved, new_map = check(m, dy, dx, (next_y, next_x, next_pos), level+1)
        if not moved:
            return (False, m)

        if next_pos == 'O':
            new_map[mover[0]][mover[1]] = '.'
            new_map[next_y][next_x] = mover[2]
            return (True, new_map)
        else:
            # big barrel
            # check direction we're pushing from
            new_map_2 = d = next_mover = None
            if dy != 0:
                # pushing big barrel up or down, need to move other half of big barrel
                if next_pos == '[':
                    d = 1
                    next_mover = ']'
                elif next_pos == ']':
                    d = -1
                    next_mover = '['
                moved2, new_map_2 = check(new_map, dy, dx, (next_y, next_x+d, next_mover), level+1)
                if not moved2:
                    return (False, m)

                new_map_2[mover[0]][mover[1]] = '.'
                new_map_2[next_y][next_x] = mover[2]
                return (True, new_map_2)
            else:
                new_map[mover[0]][mover[1]] = '.'
                new_map[next_y][next_x] = mover[2]
                return (True, new_map)
        return (False, m)
    else:
        # empty
        m[mover[0]][mover[1]] = '.'
        m[next_y][next_x] = mover[2]
        return (True, m)

def find_robot(m):
    for y, r in enumerate(m):
        if '@' in r:
            return (y, r.index('@'))
    return None

def calc(m, part2=False):
    gps = 0
    for top_dist, r in enumerate(m):
        for left_dist, pos in enumerate(r):
            if pos in ['O', '[']:
                gps += 100 * top_dist + (left_dist)
    return gps


def widen(m):
    new_map = []
    for r in m:
        cur_row = []
        for c in r:
            if c == '#':
                cur_row.append('#')
                cur_row.append('#')
            elif c == '.':
                cur_row.append('.')
                cur_row.append('.')
            elif c == 'O':
                cur_row.append('[')
                cur_row.append(']')
            elif c == '@':
                cur_row.append('@')
                cur_row.append('.')
        new_map.append(cur_row)
    return new_map

DIR = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}

if __name__ == '__main__':
    m, moves = parse()
    for idx, move in enumerate(moves):
        dy, dx = DIR[move]
        robot_pos = find_robot(m)
        _, m = check(m, dy, dx, (robot_pos[0], robot_pos[1], '@'))
    print('part1:', calc(m))

    m, moves = parse()
    m2 = widen(m)
    for idx, move in enumerate(moves):
        dy, dx = DIR[move]
        robot_pos = find_robot(m2)
        _, m2 = check(m2, dy, dx, (robot_pos[0], robot_pos[1], '@'))
    print('part2:', calc(m2, part2=True))
