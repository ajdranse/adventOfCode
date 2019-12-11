from queue import Queue
from intcode import IntCode


def print_grid(grid):
    '''prints a grid, where the grid is a dict of (x, y) to 1/0 values.  1 is painted white, 0 is black.'''
    outs = ''
    for y in range(max(grid, key=lambda g: g[1])[1] + 1):
        for x in range(max(grid, key=lambda g: g[0])[0] + 1):
            if (x, y) in grid:
                if grid[(x, y)]:
                    outs += '##'
                else:
                    outs += '  '
            else:
                outs += '  '
        outs += '\n'
    print(outs)


def run_robot(facing, pos, colour):
    inq = Queue()
    outq = Queue()
    robot = IntCode(memory.copy(), inq, outq)
    robot.start()
    grid = {}
    grid[pos] = colour
    inq.put(colour)
    DX = {0: 1, 1: 0, 2: -1, 3: 0}
    DY = {0: 0, 1: 1, 2: 0, 3: -1}
    while robot.is_alive():
        colour = outq.get()
        turn = outq.get()
        grid[pos] = colour
        facing = (facing + (1 if turn else -1)) % 4
        pos = (pos[0] + DX[facing], pos[1] + DY[facing])
        inq.put(grid[pos] if pos in grid else 0)
    return grid


with open('input') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    print('part 1')
    grid = run_robot(3, (0, 0), 0)
    print(len(grid.keys()))

    print('part 2')
    grid = run_robot(3, (0, 0), 1)
    print(len(grid.keys()))
    print_grid(grid)
