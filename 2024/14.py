import re
import math
import matplotlib.pyplot as plt

from collections import defaultdict

WIDTH = 101
HEIGHT = 103

def parse():
    with open('14.in') as f:
        inp = [x.strip() for x in f.readlines()]

    robots = []
    for l in inp:
        m = list(map(int, re.search(r'p=(\d+),(\d+) v=([0-9-]+),([0-9-]+)', l).groups()))
        pos = (m[0], m[1])
        vel = (m[2], m[3])
        robots.append((pos, vel))
    return robots

def move(robots):
    new_robots = []
    for r in robots:
        (x, y) = r[0]
        (dx, dy) = r[1]
        x2 = x + dx
        if x2 < 0 or x2 >= WIDTH:
            x2 = x2 % WIDTH
        y2 = y + dy
        if y2 < 0 or y2 >= HEIGHT:
            y2 = y2 % HEIGHT
        new_robots.append(((x2, y2), (dx,dy)))
    return new_robots

def solve(robots):
    for i in range(1, 101):
        robots = move(robots)

    mid_x = WIDTH // 2
    mid_y = HEIGHT // 2
    quadrants = [0, 0, 0, 0]
    for r in robots:
        if r[0][0] < mid_x and r[0][1] < mid_y:
            quadrants[0] += 1
        elif r[0][0] > mid_x and r[0][1] < mid_y:
            quadrants[1] += 1
        elif r[0][0] < mid_x and r[0][1] > mid_y:
            quadrants[2] += 1
        elif r[0][0] > mid_x and r[0][1] > mid_y:
            quadrants[3] += 1
    return math.prod(quadrants)

def get_state(robots):
    m = []
    for y in range(HEIGHT):
        cur_row = []
        for x in range(WIDTH):
            cur_row.append(sum([1 if r[0] == (x, y) else 0 for r in robots]))
        m.append(cur_row)
    return m

def tree(robots):
    i = 0
    while True:
        i += 1
        robots = move(robots)
        overlapping = False
        locs = defaultdict(int)
        for r in robots:
            locs[r[0]] += 1
            if locs[r[0]] > 1:
                break

        if all([v == 1 for v in locs.values()]):
            fig = plt.figure()
            im = plt.imshow(get_state(robots))
            plt.show()
            break
    return i

if __name__ == '__main__':
    robots = parse()
    print('part1:', solve(robots))
    print('part2:', tree(robots))
