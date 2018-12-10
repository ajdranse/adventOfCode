import math
import re

from itertools import combinations

def points_at(time, points, velocities):
    ret = []
    for idx, point in enumerate(points):
        ret.append((point[0] + time * velocities[idx][0], point[1] + time * velocities[idx][1]))
    return ret

def print_points(points):
    min_x = min(points, key = lambda t: t[0])[0]
    max_x = max(points, key = lambda t: t[0])[0]
    min_y = min(points, key = lambda t: t[1])[1]
    max_y = max(points, key = lambda t: t[1])[1]
    for y in xrange(min_y, max_y+1):
        row = ""
        for x in xrange(min_x, max_x+1):
            if (x, y) in points:
                row += "#"
            else:
                row += "."
        print(row)

def dist((x1, y1), (x2, y2)):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def avg_distance(points):
    distances = [dist(p1, p2) for p1, p2 in combinations(points, 2)]
    return sum(distances) / len(distances)

pattern = re.compile(r'position=<(.+), (.+)> velocity=<(.+), (.+)>')
points = []
velocities = []
with open('input') as f:
    for line in f:
        line = line.rstrip()
        m = re.match(pattern, line)
        x = int(m.group(1))
        y = int(m.group(2))
        delta_x = int(m.group(3))
        delta_y = int(m.group(4))
        points.append((x, y))
        velocities.append((delta_x, delta_y))

t = 0
cur_avg = avg_distance(points_at(t, points, velocities))
next_avg = avg_distance(points_at(t+1, points, velocities))
while next_avg < cur_avg:
    t = t + 100
    cur_avg = avg_distance(points_at(t, points, velocities))
    next_avg = avg_distance(points_at(t+1, points, velocities))

t = t - 100
min_avg = 1e6
min_t = t
for i in xrange(t, t+100):
    cur_avg = avg_distance(points_at(i, points, velocities))
    if cur_avg < min_avg:
        min_avg = cur_avg
        min_t = i
    else:
        break

min_points = points_at(min_t, points, velocities)
print_points(min_points)
print("Message at t = {}".format(min_t))
