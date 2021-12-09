import math
import queue


lines = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678',
]

with open('9.in') as f:
    lines = f.read().splitlines()

grid = {}
for y, l in enumerate(lines):
    for x, c in enumerate(l):
        grid[(x, y)] = int(c)

risk = 0
lows = []
for y in range(len(lines)):
    for x in range(len(lines[0])):
        cur = grid[(x, y)]
        if (
            cur < grid.get((x, y-1), math.inf) and
            cur < grid.get((x, y+1), math.inf) and
            cur < grid.get((x-1, y), math.inf) and
            cur < grid.get((x+1, y), math.inf)
        ):
            lows.append((x, y))
            risk += (cur + 1)
print(f'part 1: {risk}')

sizes = []
for l in lows:
    size = 0
    q = queue.Queue()
    q.put(l)

    seen = set()
    seen.add(l)
    while not q.empty():
        (x, y) = q.get()
        size += 1
        if (x+1, y) not in seen and grid.get((x+1, y), 9) != 9:
            seen.add((x+1, y))
            q.put((x+1, y))
        if (x-1, y) not in seen and grid.get((x-1, y), 9) != 9:
            seen.add((x-1, y))
            q.put((x-1, y))
        if (x, y-1) not in seen and grid.get((x, y-1), 9) != 9:
            seen.add((x, y-1))
            q.put((x, y-1))
        if (x, y+1) not in seen and grid.get((x, y+1), 9) != 9:
            seen.add((x, y+1))
            q.put((x, y+1))
    sizes.append(size)

sizes.sort()
print(f'part 2: {sizes[-1] * sizes[-2] * sizes[-3]}')
