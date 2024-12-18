import copy
import queue


SIZE = 71
def check(inp, stop):
    mem = init_mem(inp, stop)

    ex = ey = SIZE-1

    to_process = queue.Queue()
    to_process.put((0, 0, []))

    paths = []
    seen = set((0, 0))
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while not to_process.empty():
        y, x, path_so_far = to_process.get()
        if (y, x) == (ey, ex):
            # done!
            return len(path_so_far)

        path_so_far.append((y, x))
        for dy, dx in DIRS:
            if y+dy >= 0 and y+dy < len(mem) and x+dx >= 0 and x+dx < len(mem[0]) and mem[y+dy][x+dx] != '#' and (y+dy, x+dx) not in seen:
                seen.add((y+dy, x+dx))
                to_process.put((y + dy, x + dx, copy.deepcopy(path_so_far)))
    return None

def init_mem(inp, stop):
    mem = []
    for _ in range(SIZE):
        mem.append(['.'] * SIZE)

    for idx in range(stop+1):
        x, y = inp[idx]
        mem[y][x] = '#'

    return mem

with open('18.in') as f:
    inp = [list(map(int, x.strip().split(','))) for x in f.readlines()]

print('part1:', check(inp, 1024))

high = len(inp)
low = 1024

p = None
while low < high-1:
    mid = (low + high) // 2
    p = check(inp, mid)
    if p is None:
        # failure, check low half
        high = mid - 1
    else:
        # success, check high half
        low = mid
while p is not None:
    # we're at last success now, so print out next byte
    mid += 1
    p = check(inp, mid)
print('part2:', ','.join([str(c) for c in inp[mid]]))
