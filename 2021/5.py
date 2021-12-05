def go(lines, p2):
    # didn't see numbers bigger than 1000 in input
    max_x = 1000
    max_y = 1000
    grid = [[0 for x in range(max_x+1)] for y in range(max_y+1)]
    for l in lines:
        s = l.split(' -> ')
        (x, y) = [int(i) for i in s[0].split(',')]
        (x2, y2) = [int(i) for i in s[1].split(',')]
        delta_x = 0
        delta_y = 0
        if x == x2:
            delta_y = 1 if y2 > y else -1
        elif y == y2:
            delta_x = 1 if x2 > x else -1
        else:
            if (p2):
                delta_y = 1 if y2 > y else -1
                delta_x = 1 if x2 > x else -1
            else:
                continue

        grid[y][x] += 1
        while (x, y) != (x2, y2):
            y += delta_y
            x += delta_x
            grid[y][x] += 1

    # find all entries in grid >= 2
    return sum([1 if x >= 2 else 0 for y in grid for x in y])

if __name__ == '__main__':
    lines = []
    with open('5.in') as f:
        lines = f.read().splitlines()

    ret = go(lines, False)
    print(f'part 1: {ret}')
    ret = go(lines, True)
    print(f'part 2: {ret}')
