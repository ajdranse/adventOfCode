with open('20.in') as f:
    lines = f.read().splitlines()
alg = lines[0]
lines = lines[2:]

def apply_alg(grid, xmin, xmax, ymin, ymax, default):
    ds = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    ret = {}
    for x in range(xmin - 2, xmax + 3):
        for y in range(ymin - 2, ymax + 3):
            val = ''
            for d in ds:
                val += str(grid.get((x + d[0], y + d[1]), default))
            ret[(x, y)] = 1 if alg[int(val, 2)] == '#' else 0
    return (ret, xmin - 2, xmax + 2, ymin - 2, ymax + 2)

grid = {}
y = 0
for l in lines:
    x = 0
    for c in l:
        grid[(x, y)] = 1 if c == '#' else 0
        x += 1
    y += 1

ymax = y
xmax = x

xmin = 0
ymin = 0

step = 0
while step < 50:
    # value of 0 in algorithm maps to 1, value of 511 is 0, so the infinite bits flip every iteration
    (grid, xmin, xmax, ymin, ymax) = apply_alg(grid, xmin, xmax, ymin, ymax, step % 2)
    step += 1

    if step == 2:
        lit = 0
        for k, v in grid.items():
            lit += v

        print(f'part1: {lit}')

lit = 0
for k, v in grid.items():
    lit += v

print(f'part2: {lit}')

