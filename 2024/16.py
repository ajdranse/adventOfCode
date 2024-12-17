import queue


DIRS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def print_path(path, m):
    for y, x, d, c in path:
        if m[y][x] in ['.', '>', '<', '^', 'v']:
            m[y][x] = d
        elif m[y][x] in ['S', 'E']:
            pass
        else:
            raise ValueError(m[y][x])

    for r in m:
        print(''.join(r))

def parse():
    with open('16.in') as f:
        inp = [x.strip() for x in f.readlines()]

    m = []
    s = None
    e = None
    for y, l in enumerate(inp):
        m.append([c for c in l])
        if 'S' in l:
            s = (y, l.index('S'))
        if 'E' in l:
            e = (y, l.index('E'))
    return (m, s, e)

def get_all_moves(y, x, d, cost):
    r = []
    if d == '^' or d == 'v':
        r.append((y, x, '>', cost+1000))
        r.append((y, x, '<', cost+1000))
    if d == '<' or d == '>':
        r.append((y, x, '^', cost+1000))
        r.append((y, x, 'v', cost+1000))
    dy, dx = DIRS[d]
    r.append((y + dy, x + dx, d, cost+1))
    return r

if __name__ == '__main__':
    (m, s, e) = parse()

    seen = {}
    paths = []
    to_process = queue.Queue()
    to_process.put((s[0], s[1], '>', [(s[0], s[1], '>', 0)], 0))
    while not to_process.empty():
        (y, x, d, so_far, cost) = to_process.get()
        if m[y][x] == '#':
            # dead end
            continue
        if (y, x) == e:
            # made end, yay
            new_path = so_far.copy()
            new_path.append((y, x, d, cost))
            paths.append(new_path)
        else:
            for (ny, nx, nd, new_cost) in get_all_moves(y, x, d, cost):
                if (ny, nx, nd) not in seen or seen[(ny, nx, nd)] >= new_cost:
                    seen[(ny, nx, nd)] = new_cost
                    new_path = so_far.copy()
                    new_path.append((ny, nx, nd, new_cost))
                    to_process.put((ny, nx, nd, new_path, new_cost))
    min_path = None
    min_score = None
    seats = set()
    for p in paths:
        if min_score is None or p[-1][3] < min_score:
            seats = set([(y, x) for y, x, _, _ in p])
            min_path = p
            min_score = p[-1][3]
        if p[-1][3] == min_score:
            seats.update([(y, x) for y, x, _, _ in p])

    print('part1:', min_score)
    print('part2:', len(seats))
