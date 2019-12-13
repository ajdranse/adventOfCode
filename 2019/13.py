from queue import Queue
from intcode import IntCode


def print_grid(grid):
    '''prints a grid, where the grid is a dict of (x, y) to 1/0 values.  1 is painted white, 0 is black.
        0 is an empty tile. No game object appears in this tile.
        1 is a wall tile. Walls are indestructible barriers.
        2 is a block tile. Blocks can be broken by the ball.
        3 is a horizontal paddle tile. The paddle is indestructible.
        4 is a ball tile. The ball moves diagonally and bounces off objects.
    '''
    outs = ''
    for y in range(max(grid, key=lambda g: g[1])[1] + 1):
        for x in range(max(grid, key=lambda g: g[0])[0] + 1):
            if (x, y) in grid:
                if grid[(x, y)] == 1:
                    outs += 'w'
                elif grid[(x, y)] == 2:
                    outs += '#'
                elif grid[(x, y)] == 3:
                    outs += '-'
                elif grid[(x, y)] == 4:
                    outs += 'o'
                else:
                    outs += ' '
            else:
                outs += ' '
        outs += '\n'
    outs += str(grid[(-1, 0)]) + '\n'
    print(outs)


with open('13.in') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    inq = Queue()
    outq = Queue()
    t = IntCode(memory.copy(), inq, outq)
    t.start()
    blocks = 0
    grid = {}
    while t.is_alive():
        (x, y, i) = (outq.get(), outq.get(), outq.get())
        grid[(x, y)] = i
    t.join()

    blocks = 0
    for pos, tile in grid.items():
        if tile == 2:
            blocks += 1
    print('part 1: ', blocks)

with open('13.in') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    print('part 2')
    inq = Queue()
    outq = Queue()
    memory[0] = 2
    t = IntCode(memory.copy(), inq, outq)
    t.start()
    blocks = 0
    grid = {}
    ball_pos = None
    paddle_pos = None
    inq.put(0)
    last_blocks = 0
    while t.is_alive():
        (x, y, i) = (outq.get(), outq.get(), outq.get())
        grid[(x, y)] = i
        if i == 4:
            # ball
            ball_pos = (x, y)
            if paddle_pos:
                if ball_pos == paddle_pos:
                    inq.put(0)
                elif ball_pos[0] < paddle_pos[0]:
                    inq.put(-1)
                elif ball_pos[0] > paddle_pos[0]:
                    inq.put(1)
                print_grid(grid)
        elif i == 3:
            # paddle
            paddle_pos = (x, y)

    t.join()
    while not outq.empty():
        (x, y, i) = (outq.get(), outq.get(), outq.get())
        grid[(x, y)] = i
    print_grid(grid)
