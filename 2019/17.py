from queue import Queue
from intcode import IntCode


def to_grid(inp):
    grid = {}
    x = y = 0
    for c in inp:
        if c == '\n':
            y += 1
            x = 0
        else:
            grid[(x, y)] = c
            x += 1
    return grid


def get_opposite(d):
    if d == 'v':
        return '^'
    elif d == '^':
        return 'v'
    elif d == '<':
        return '>'
    elif d == '>':
        return '<'


def get_turn(old_d, new_d):
    if (
        (old_d == '^' and new_d == '>') or (old_d == 'v' and new_d == '<') or
        (old_d == '<' and new_d == '^') or (old_d == '>' and new_d == 'v')
    ):
        return 'R'
    elif (
        (old_d == '^' and new_d == '<') or (old_d == 'v' and new_d == '>') or
        (old_d == '<' and new_d == 'v') or (old_d == '>' and new_d == '^')
    ):
        return 'L'

    raise Exception('unknown transition from {} to {}'.format(old_d, new_d))


def walk(grid, pos, direction):
    DX = {'^': 0, 'v': 0, '>': 1, '<': -1}
    DY = {'^': -1, 'v': 1, '>': 0, '<': 0}
    seen = []
    intersections = []
    moves = []
    while True:
        length = 0
        while grid.get(pos, None) and grid[pos] == '#':
            if pos in seen:
                intersections.append(pos)
            else:
                seen.append(pos)
            pos = (pos[0] + DX[direction], pos[1] + DY[direction])
            length += 1
        if length:
            moves.append(length)
            # undo last move, which failed
            pos = (pos[0] - DX[direction], pos[1] - DY[direction])

        # try to find a turn
        for i in DX.keys():
            if i != get_opposite(direction):
                test_pos = (pos[0] + DX[i], pos[1] + DY[i])
                if grid.get(test_pos) and grid[test_pos] == '#':
                    moves.append(get_turn(direction, i))
                    direction = i
                    pos = test_pos
                    break
        else:
            # no turn found, so we must be done
            print('intersections: ', intersections)
            print('moves: ', moves)
            return intersections


with open('17.in') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    inq = Queue()
    outq = Queue()
    t = IntCode(memory.copy(), inq, outq)
    t.start()
    raw_grid = []
    while t.is_alive():
        raw_grid.append(outq.get())
    grid_len = len(raw_grid)
    t.join()
    scaffolds = ''.join([str(chr(x)) for x in raw_grid])
    grid = to_grid(scaffolds)
    robot_pos = None
    robot_pos = [(x, y) for (x, y), c in grid.items() if c in ['v', '^', '<', '>']][0]
    intersections = walk(grid, robot_pos, grid[robot_pos])
    print('part1:', sum(i[0] * i[1] for i in intersections))

    # hand made the move functions
    # A = ['R', 6, 'L', 12, 'R', 6]
    A = [82, 44, 54, 44, 76, 44, 49, 50, 44, 82, 44, 54, 10]
    # B = ['L', 12, R, 6, L, 8, L, 12]
    B = [76, 44, 49, 50, 44, 82, 44, 54, 44, 76, 44, 56, 44, 76, 44, 49, 50, 10]
    # C = [R, 12, L, 10, L, 10]
    C = [82, 44, 49, 50, 44, 76, 44, 49, 48, 44, 76, 44, 49, 48, 10]
    # main_routine=[A,      A,      B,      C,      B,      C,      B,      C,      B,      A]
    main_routine = [65, 44, 65, 44, 66, 44, 67, 44, 66, 44, 67, 44, 66, 44, 67, 44, 66, 44, 65, 10]

    part2 = memory.copy()
    part2[0] = 2
    inq = Queue()
    outq = Queue()
    t = IntCode(part2, inq, outq)
    t.start()
    for i in main_routine:
        inq.put(i)
    for i in A:
        inq.put(i)
    for i in B:
        inq.put(i)
    for i in C:
        inq.put(i)
    inq.put(110)
    inq.put(10)
    t.join()
    line = ''
    while not outq.empty():
        dust = outq.get()
    print('part2:', dust)
