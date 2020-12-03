grid = []
# with open("3.test") as f:
with open("3.in") as f:
    for line in f.read().splitlines():
        grid.append([0 if x == "." else 1 for x in line])

product = 1
ds = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for d in ds:
    hit = 0
    x = 0
    y = 0
    while y < len(grid):
        hit += grid[y][x]
        x = (x + d[0]) % len(grid[y])
        y += d[1]
    if d[0] == 3:
        print("part 1: {}".format(hit))
    product *= hit
print("part 2: {}".format(product))
