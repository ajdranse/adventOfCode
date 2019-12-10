from collections import defaultdict
from math import atan2, pi


def get_slopes(asteroids, point):
    RADS_TO_DEGS = 180 / pi
    slopes = defaultdict(list)
    for a in asteroids:
        if a != point:
            slope = atan2(a[1] - point[1], a[0] - point[0]) * RADS_TO_DEGS
            if slope < 0:
                slope = 360 + slope
            dist = abs(a[1] - point[1]) + abs(a[0] - point[0])
            slopes[slope].append((dist, a))
    return slopes


def get_asteroids(filename):
    asteroids = []
    with open(filename) as f:
        y = 0
        line = f.readline().strip()
        while line:
            x = 0
            for c in line:
                if c == '#':
                    asteroids.append((x, y))
                x += 1
            y += 1
            line = f.readline().strip()
    return asteroids


def part1(filename):
    asteroids = get_asteroids(filename)
    slopes = {}
    for a in asteroids:
        slopes[a] = get_slopes(asteroids, a)

    max_see = 0
    best = None
    for k in slopes.keys():
        if len(slopes[k]) > max_see:
            max_see = len(slopes[k])
            best = k
    return best, max_see


def part2(filename, station):
    asteroids = get_asteroids(filename)
    slopes = get_slopes(asteroids, station)
    aim = 270.0
    removed = 0
    while True:
        for s in slopes.keys():
            if s >= aim and len(slopes[s]) > 0:
                aim = s
                to_kill = min(slopes[s], key=lambda s: s[0])
                slopes[s].remove(to_kill)
                removed += 1
                if removed == 200:
                    return to_kill[1]
                asteroids.remove(to_kill[1])
                if len(asteroids) == 0:
                    return None
        aim = 0


# for i in ['test.1', 'test.2', 'test.3', 'test.4', 'test.5']:
#     print(i, part1(i))

print('part1', part1('input')[0])
res = part2('input', part1('input')[0])
print('part2', res[0]*100 + res[1])
