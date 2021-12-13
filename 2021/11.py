def check_flash(grid, flashed):
    any_flashed = False
    for y in range(10):
        for x in range(10):
            if grid[(x, y)] > 9 and (x, y) not in flashed:
                any_flashed = True
                flashed.add((x, y))
                for dy in dys:
                    for dx in dxs:
                        if dy == dx == 0:
                            pass
                        if x + dx >= 0 and x + dx < 10 and y + dy >= 0 and y + dy < 10:
                            grid[(x + dx, y + dy)] += 1
    return any_flashed


with open('11.in') as f:
    lines = f.read().splitlines()

grid = {}
y = 0
for l in lines:
    x = 0
    for c in l:
        grid[(x, y)] = int(c)
        x += 1
    y += 1

dxs = [-1, 0, 1]
dys = [-1, 0, 1]

flashes = 0
step = 0
all_flashed = False
while not all_flashed:
    for y in range(10):
        for x in range(10):
            grid[(x, y)] += 1

    flashed = set()
    any_flashed = check_flash(grid, flashed)
    while any_flashed:
        any_flashed = check_flash(grid, flashed)

    this_flashes = 0
    for y in range(10):
        for x in range(10):
            if grid[(x, y)] > 9:
                grid[(x, y)] = 0
                this_flashes += 1
    if step < 100:
        flashes += this_flashes
    if this_flashes == 100:
        all_flashed = True
    step += 1

print(f'part1: {flashes}')
print(f'part2: {step}')
