def do_move(h, t):
    x_diff = h[0] - t[0]
    y_diff = h[1] - t[1]

    if abs(x_diff) > 1 or abs(y_diff) > 1 or abs(x_diff) + abs(y_diff) > 2:
        dx = x_diff / abs(x_diff) if x_diff != 0 else 0
        dy = y_diff / abs(y_diff) if y_diff != 0 else 0
        t = (t[0] + dx, t[1] + dy)

    return t


def run(moves, sz):
    moves = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }

    knots = [(0, 0) for x in range(sz)]
    visited = set()

    for move in moves:
        (dx, dy) = moves[move.split()[0]]
        for n in range(int(move.split()[1])):
            knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
            for i in range(len(knots)-1):
                knots[i+1] = do_move(knots[i], knots[i+1])
            visited.add(knots[-1])
    return len(visited)


lines = []
with open('9.in') as f:
    lines = [x.strip() for x in f.readlines()]

print('part1', run(lines, 2))
print('part2', run(lines, 10))
