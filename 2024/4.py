DIRS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 0),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

arr = []
with open('4.in') as f:
    inp = [list(x.strip()) for x in f.readlines()]

found = 0
found2 = 0
for y in range(len(inp)):
    for x in range(len(inp[y])):
        for (dy, dx) in DIRS:
            if len(inp) > y + 3*dy and len(inp[y]) > x + 3 * dx and y + 3 * dy >= 0 and x + 3 * dx >= 0:
                if all([inp[y + i*dy][x + i*dx] == c for i, c in enumerate('XMAS')]):
                    found += 1

        if inp[y][x] == 'A':
            if y-1 >= 0 and y+1 < len(inp) and x-1 >= 0 and x+1 < len(inp[y]):
                if (inp[y-1][x-1] == 'M' and inp[y+1][x+1] == 'S') or (inp[y-1][x-1] == 'S' and inp[y+1][x+1] == 'M'):
                    if (inp[y-1][x+1] == 'M' and inp[y+1][x-1] == 'S') or (inp[y-1][x+1] == 'S' and inp[y+1][x-1] == 'M'):
                        found2 += 1

print('part1:', found)
print('part2:', found2)
