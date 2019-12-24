from collections import defaultdict
from intcode import print_grid


def step(grid, width, height):
    newgrid = defaultdict(int)
    for y in range(height):
        for x in range(width):
            adjacent = grid[(x-1, y)] + grid[(x+1, y)] + grid[(x, y-1)] + grid[(x, y+1)]
            #A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
            if grid[(x, y)] == 1 and adjacent == 1:
                newgrid[(x, y)] = 1
            #An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
            elif grid[(x, y)] == 0 and (adjacent == 1 or adjacent == 2):
                newgrid[(x, y)] = 1
            else:
                newgrid[(x, y)] = 0
    return newgrid


def step2(grid, width, height, start, stop):
    newgrid = defaultdict(int)
    for d in range(start-1, stop+1):
        for y in range(height):
            for x in range(width):
                if x == 2 and y == 2:
                    continue
                left = [(x-1, y, d)]
                right = [(x+1, y, d)]
                up = [(x, y-1, d)]
                down = [(x, y+1, d)]
                if x == 3 and y == 2:
                    left = [(4, y2, d+1) for y2 in range(5)]
                if x == 1 and y == 2:
                    right = [(0, y2, d+1) for y2 in range(5)]
                if x == 2 and y == 3:
                    up = [(x2, 4, d+1) for x2 in range(5)]
                if x == 2 and y == 1:
                    down = [(x2, 0, d+1) for x2 in range(5)]

                if x == 0:
                    left = [(1, 2, d-1)]
                if x == 4:
                    right = [(3, 2, d-1)]
                if y == 0:
                    up = [(2, 1, d-1)]
                if y == 4:
                    down = [(2, 3, d-1)]

                tocheck = []
                tocheck.extend(left)
                tocheck.extend(right)
                tocheck.extend(up)
                tocheck.extend(down)
                adjacent = 0
                for pos in tocheck:
                    adjacent += grid[pos]
                #A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
                if grid[(x, y, d)] == 1 and adjacent == 1:
                    newgrid[(x, y, d)] = 1
                #An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
                elif grid[(x, y, d)] == 0 and (adjacent == 1 or adjacent == 2):
                    newgrid[(x, y, d)] = 1
                else:
                    newgrid[(x, y, d)] = 0
    return newgrid


def run(filename):
    grid = defaultdict(int)
    maxy = 0
    maxx = 0
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        y = 0
        for l in lines:
            x = 0
            for c in l:
                if c == '#':
                    grid[(x, y)] = 1
                else:
                    grid[(x, y)] = 0
                x += 1
            y += 1
            maxx = x
        maxy = y
    seen = []
    grid_vals = {0: '.', 1: '#'}
    for _ in range(100):
        grid = step(grid, maxx, maxy)
        if grid in seen:
            score = 0
            for y in range(maxy):
                for x in range(maxx):
                    if grid[(x, y)]:
                        score += pow(2, y*5 + x)
            print('part1', score)
            break
        else:
            seen.append(grid.copy())


def run2(filename):
    grid = defaultdict(int)
    maxy = 0
    maxx = 0
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        y = 0
        for l in lines:
            x = 0
            for c in l:
                if c == '#':
                    grid[(x, y, 0)] = 1
                else:
                    grid[(x, y, 0)] = 0
                x += 1
            y += 1
            maxx = x
        maxy = y
    grid_vals = {0: '.', 1: '#'}
    mindepth = min(d for (_, _, d) in grid)
    maxdepth = max(d for (_, _, d) in grid)
    for i in range(200):
        grid = step2(grid, maxx, maxy, mindepth, maxdepth+1)
        mindepth = min(d for (_, _, d) in grid)
        maxdepth = max(d for (_, _, d) in grid)
    print('part2', sum(grid.values()))

# run('24.test')
run('24.in')
run2('24.in')
