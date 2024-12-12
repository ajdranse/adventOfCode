import queue

from collections import defaultdict
from itertools import combinations

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def parse():
    with open('12.in') as f:
        inp = [list(x.strip()) for x in f.readlines()]

    regions = []
    seen = set()
    to_process = queue.Queue()
    for r in range(len(inp)):
        for c in range(len(inp[r])):
            if (r, c) in seen:
                continue

            seen.add((r, c))
            cur_region = [(r, c)]
            cur_type = inp[r][c]

            for d in DIRS:
                to_process.put((r + d[0], c + d[1]))
            while not to_process.empty():
                (y, x) = to_process.get()
                if (y, x) not in seen and y >= 0 and y < len(inp) and x >= 0 and x < len(inp[0]) and inp[y][x] == cur_type:
                    cur_region.append((y, x))
                    seen.add((y, x))
                    for d in DIRS:
                        to_process.put((y + d[0], x + d[1]))
            regions.append(cur_region)
    return regions

def part1(regions):
    price = 0
    for r in regions:
        area = len(r)
        # assume every point is totally disjoint (won't be true)
        perimeter = area * 4
        for a, b in combinations(r, 2):
            # if two points are next to each other, remove 2 from the perimeter (the edges that don't exist)
            if abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1:
                perimeter -= 2
        price += (area * perimeter)
    return price

def part2(regions):
    price = 0
    for idx, region in enumerate(regions):
        # determine horizontal sides
        # walk every row
        #  - every time it switches from having same type above to none/diff above is a north wall
        #  - every time it switches from having same type below to none/diff below is a south wall
        # determine vertical sides
        #  - it will have same # of vertical sides as horizontal

        sides = 0
        r = sorted(region, key=lambda x: (x[0], x[1]))
        for y in range(min([p[0] for p in r]), max([p[0] for p in r]) + 1):
            up_edge = False
            down_edge = False
            row = [p for p in r if p[0] == y]
            # for each point in this row
            for x in range(min([p[1] for p in row]), max([p[1] for p in row]) + 1):
                if (y, x) in row:
                    # check up
                    if (y-1, x) not in r:
                        up_edge = True
                    elif up_edge:
                        sides += 1
                        up_edge = False
                    # check down
                    if (y+1, x) not in r:
                        down_edge = True
                    elif down_edge:
                        sides += 1
                        down_edge = False
                else:
                    sides += sum([up_edge, down_edge])
                    up_edge = False
                    down_edge = False
            sides += sum([up_edge, down_edge])
        sides *= 2
        price += (len(r) * sides)
    return price

if __name__ == '__main__':
    regions = parse()
    print('part1:', part1(regions))
    print('part2:', part2(regions))
