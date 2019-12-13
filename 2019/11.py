from queue import Queue
from intcode import IntCode, print_grid


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


with open('11.in') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    print('part 1')
    grid = run_robot(3, (0, 0), 0)
    print(len(grid.keys()))

    print('part 2')
    grid = run_robot(3, (0, 0), 1)
    print(len(grid.keys()))
    print_grid(grid, {0: '  ', 1: '##'})
