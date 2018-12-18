def get_next(grid, x, y):
    num_trees = 0
    num_lumberyards = 0
    num_open = 0
    for dy in xrange(-1, 2):
        if y + dy < 0 or y + dy >= len(grid):
            continue
        for dx in xrange(-1, 2):
            if x + dx < 0 or x + dx >= len(max(grid)):
                continue
            n = grid[y + dy][x + dx]
            if n == '.':
                num_open += 1
            elif n == '|':
                num_trees += 1
            elif n == '#':
                num_lumberyards += 1
    cur = grid[y][x]
    if cur == '.' and num_trees >= 3:
        return '|'
    elif cur == '|' and num_lumberyards >= 3:
        return '#'
    elif cur == '#':
        if num_lumberyards >= 2 and num_trees >= 1:
            return '#'
        else:
            return '.'
    else:
        return cur


def get_next_grid(grid):
    new_grid = [['' for x in xrange(len(max(grid)))] for y in xrange(len(grid))]
    for y in xrange(len(grid)):
        for x in xrange(len(max(grid))):
            new_grid[y][x] = get_next(grid, x, y)
    return new_grid


def print_grid(grid):
    for y in xrange(len(grid)):
        string = ""
        for x in xrange(len(max(grid))):
            string += grid[y][x]
        print string


grid = []
with open('input') as f:
    for line in f:
        line = line.rstrip()
        grid.append(line)

flattened_grid = [item for sublist in grid for item in sublist]
flattened_str = ''.join(flattened_grid)
wooded = len([x for x in flattened_grid if x == '|'])
lumberyards = len([x for x in flattened_grid if x == '#'])

cache = []
for i in xrange(1, 500):
    if i % 10 == 0:
        print(i)
    grid = get_next_grid(grid)
    flattened = ''.join(''.join(row) for row in grid)
    if flattened in cache:
        cache_idx = cache.index(flattened) + 1 # list index is 0-based
        print("Found cycle, current iteration {} is repeat of {}".format(i, cache_idx))
        period = i - cache_idx
        while cache_idx % period != 1000000000 % period:
            cache_idx += 1
        print("Index {} has same remainder ({}) as 1000000000: {}".format(cache_idx, cache_idx % period, 1000000000 % period))
        wooded = len([x for x in cache[cache_idx-1] if x == '|'])
        lumberyards = len([x for x in cache[cache_idx-1] if x == '#'])
        print("Part 2: {}*{} = {}".format(wooded, lumberyards, wooded * lumberyards))
        break
    cache.append(flattened)

    if i == 10:
        wooded = len([x for x in flattened if x == '|'])
        lumberyards = len([x for x in flattened if x == '#'])
        print("Part 1: {}*{} = {}".format(wooded, lumberyards, wooded * lumberyards))
