from queue import Queue
from intcode import print_grid, IntCode

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

grid_values = {0: ' ', 1: '█', 2: '#', 3: '-', 4: 'o'}

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
                print_grid(grid, grid_values)
        elif i == 3:
            # paddle
            paddle_pos = (x, y)

    t.join()
    while not outq.empty():
        (x, y, i) = (outq.get(), outq.get(), outq.get())
        grid[(x, y)] = i
    print_grid(grid, grid_values)
    print(grid[(-1, 0)])
