from copy import deepcopy

grid = []
with open("11.in") as f:
# with open("11.test") as f:
    for line in f:
        grid.append([c for c in line.rstrip()])

width = len(grid[0])
height = len(grid)
def do(grid, part1):
    while True:
        # for r in grid:
        #     print(''.join(r))
        # print('')

        newgrid = deepcopy(grid)
        changed = False
        for y in range(height):
            for x in range(width):
                neighbors = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if not(dy == 0 and dx == 0):
                            new_y = y + dy
                            new_x = x + dx
                            if not part1:
                                while 0 <= new_y < height and 0 <= new_x < width and grid[new_y][new_x] == '.':
                                    new_y = new_y + dy
                                    new_x = new_x + dx
                            if 0 <= new_y < height and 0 <= new_x < width and grid[new_y][new_x] == '#':
                                neighbors += 1
                # if this is an empty seat
                if grid[y][x] == 'L' and neighbors == 0:
                    # all are unoccupied
                    newgrid[y][x] = '#'
                    changed = True
                elif grid[y][x] == '#' and neighbors >= (4 if part1 else 5):
                    # more than 4 occupied neighbors
                    newgrid[y][x] = 'L'
                    changed = True
        if not changed:
            break
        grid = deepcopy(newgrid)
        # for r in grid:
        #     print(''.join(r))
        # print('')

    occupied = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '#':
                occupied += 1
    return occupied

print('part1: {}'.format(do(grid, True)))
print('part2: {}'.format(do(grid, False)))
