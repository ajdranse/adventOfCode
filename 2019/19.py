from intcode import print_grid, IntCode
from queue import Queue


# print('part1')
# with open('19.in') as f:
#     memory = [int(x.strip()) for x in f.read().split(',')]
#     inq = Queue()
#     outq = Queue()
#     grid = {}
#     for y in range(50):
#         for x in range(50):
#             t = IntCode(memory.copy(), inq, outq)
#             t.start()
#             inq.put(x)
#             inq.put(y)
#             res = outq.get()
#             grid[(x, y)] = res
#     grid_vals = {0: '.', 1: '#'}
#     print_grid(grid, grid_vals)
#     print(sum(grid.values()))

def valid(x, y, memory):
    inq = Queue()
    outq = Queue()
    t = IntCode(memory.copy(), inq, outq)
    t.start()
    inq.put(x)
    inq.put(y)
    t.join()
    return outq.get()

print('part2')
with open('19.in') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    x = 0
    y = 1100
    done = False
    while not done:
        # find beginning on this row
        while not valid(x, y, memory):
            x += 1

        # find end on this row
        x2 = x + 99
        while valid(x2, y, memory):
            x2 += 1

        # if beam is wide enough, check bottom left using end of beam
        if x2 - x >= 100:
            if valid(x2 - 100, y+99, memory):
                # see if there's a closer origin
                for xp in range(x2 - 101, x, -1):
                    if not valid(xp, y+99, memory):
                        print('top left corner ({}, {})'.format((xp+1), y))
                        done = True
                        break
                else:
                    print('top left corner ({}, {})'.format(x, y))
                    done = True
                    break
        y += 1
