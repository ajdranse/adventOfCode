from queue import Queue
from intcode import IntCode

with open('input') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    print('part 1')
    inq = Queue()
    outq = Queue()
    robot = IntCode(memory.copy(), inq, outq)
    robot.start()
    pos = (0, 0)
    facing = 270
    grid = {}
    grid[pos] = 1
    inq.put(1)
    while robot.is_alive():
        colour = outq.get()
        turn = outq.get()
        grid[pos] = colour
        if turn:
            facing = (facing + 90) % 360
        else:
            facing = (facing - 90) % 360
        if facing == 0:
            pos = (pos[0] + 1, pos[1])
        elif facing == 90:
            pos = (pos[0], pos[1] + 1)
        elif facing == 180:
            pos = (pos[0] - 1, pos[1])
        elif facing == 270:
            pos = (pos[0], pos[1] - 1)
        if pos in grid:
            inq.put(grid[pos])
        else:
            inq.put(0)

    robot.join()
    print(len(grid))

    print('part 2')
    x_min = 999
    x_max = 0
    y_min = 999
    y_max = 0
    for p in grid.keys():
        if p[0] > x_max:
            x_max = p[0]
        if p[0] < x_min:
            x_min = p[0]
        if p[1] > y_max:
            y_max = p[1]
        if p[1] < y_min:
            y_min = p[1]

    for y in range(y_min, y_max+1):
        outs = ''
        for x in range(x_min, x_max+1):
            if (x, y) in grid:
                if grid[(x, y)]:
                    outs += '#'
                else:
                    outs += '.'
            else:
                outs += '.'
        print(outs)
