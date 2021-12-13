def dots(grid, max_x, max_y):
    dots = 0
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in grid and grid[(x, y)] == 1:
                dots += 1
    return dots


def print_grid(grid, max_x, max_y):
    for y in range(max_y + 1):
        s = ''
        for x in range(max_x + 1):
            if (x, y) in grid and grid[(x, y)] == 1:
                s += '#'
            else:
                s += '.'
        print(s)


lines = [
'6,10',
'0,14',
'9,10',
'0,3',
'10,4',
'4,11',
'6,0',
'6,12',
'4,1',
'0,13',
'10,12',
'3,4',
'3,0',
'8,4',
'1,10',
'2,14',
'8,10',
'9,0',
'',
'fold along y=7',
'fold along x=5',
]

with open('13.in') as f:
    lines = f.read().splitlines()

grid_lines = []
instrs = []
for l in lines:
    if ',' in l:
        grid_lines.append(l)
    elif 'fold' in l:
        instrs.append(l)

max_x = 0
max_y = 0
grid = {}
for l in grid_lines:
    (x, y) = l.split(',')
    if int(x) > max_x:
        max_x = int(x)
    if int(y) > max_y:
        max_y = int(y)

    grid[(int(x), int(y))] = 1

after_first = 0
for i in instrs:
    (d, n) = i.split(' ')[2].split('=')

    if d == 'y':
        new_y = 0
        for y in range (max_y, int(n), -1):
            for x in range(max_x+1):
                if (x, y) in grid and grid[(x, y)] == 1:
                    grid[(x, new_y)] = 1
                    grid[(x, y)] = 0
            new_y += 1
        max_y = int(n) - 1
    elif d == 'x':
        new_x = 0
        for y in range(max_y + 1):
            new_x = 0
            for x in range(max_x, int(n), -1):
                if (x, y) in grid and grid[(x, y)] == 1:
                    grid[(new_x, y)] = 1
                    grid[(x, y)] = 0
                new_x += 1
        max_x = int(n) - 1
    if after_first == 0:
        after_first = dots(grid, max_x, max_y)

print(f'part1: {after_first}')
print_grid(grid, max_x, max_y)
