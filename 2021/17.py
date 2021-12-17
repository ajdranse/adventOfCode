import re

# inp = 'target area: x=20..30, y=-10..-5'
inp = 'target area: x=150..193, y=-136..-86'

m = re.search('target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', inp)
if m:
    xmin = int(m.group(1))
    xmax = int(m.group(2))
    ymin = int(m.group(3))
    ymax = int(m.group(4))

max_y = 0
vel = None

in_target = set()

min_x_start = 0
max_x_start = 0
for x in range(0, xmax+1):
    for y in range(-1000, 1000):
        max_y_pos = 0
        y_velocity = y
        y_pos = 0

        x_velocity = x
        x_pos = 0

        while x_pos < xmax and y_pos > ymin:
            y_pos += y_velocity
            if y_pos > max_y_pos:
                max_y_pos = y_pos

            y_velocity -= 1

            x_pos += x_velocity
            if x_velocity > 0:
                x_velocity -= 1
            if x_velocity < 0:
                x_velocity += 1

            if ymin <= y_pos <= ymax and xmin <= x_pos <= xmax:
                in_target.add((x, y))
                if max_y_pos > max_y:
                    max_y = max_y_pos
                    vel = (x, y)
print('part1', max_y, vel)
print('part2', len(in_target))
