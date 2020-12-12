import math


moves = []
# with open("12.test") as f:
with open("12.in") as f:
    moves = [line.rstrip() for line in f]

direction = 90
pos = (0, 0)
for move in moves:
    act = move[0]
    val = int(''.join(move[1:]))

    if act == 'N':
        pos = (pos[0], pos[1] + val)
    elif act == 'S':
        pos = (pos[0], pos[1] - val)
    elif act == 'E':
        pos = (pos[0] + val, pos[1])
    elif act == 'W':
        pos = (pos[0] - val, pos[1])
    elif act == 'L':
        direction = (direction - val) % 360
    elif act == 'R':
        direction = (direction + val) % 360
    elif act == 'F':
        if direction == 0:
            # move north
            pos = (pos[0], pos[1] + val)
        elif direction == 90:
            # move east
            pos = (pos[0] + val, pos[1])
        elif direction == 180:
            # move south
            pos = (pos[0], pos[1] - val)
        elif direction == 270:
            # move west
            pos = (pos[0] - val, pos[1])
    else:
        raise('unknown action: {}'.format(act))

print('part1: {}'.format(abs(pos[0]) + abs(pos[1])))

pos = (0, 0)
waypoint = (10, 1)
for move in moves:
    act = move[0]
    val = int(''.join(move[1:]))

    if act == 'N':
        waypoint = (waypoint[0], waypoint[1] + val)
    elif act == 'S':
        waypoint = (waypoint[0], waypoint[1] - val)
    elif act == 'E':
        waypoint = (waypoint[0] + val, waypoint[1])
    elif act == 'W':
        waypoint = (waypoint[0] - val, waypoint[1])
    elif act == 'L' or act == 'R':
        rads = math.radians(-val if act == 'R' else val)
        cos = math.cos(rads)
        sin = math.sin(rads)
        x, y = waypoint
        waypoint = (cos * x - sin * y, sin * x + cos * y)  # rotate about origin
    elif act == 'F':
        pos = (pos[0] + val * waypoint[0], pos[1] + val * waypoint[1])
    else:
        raise('unknown action: {}'.format(act))
print('part2: {}'.format(int(abs(pos[0]) + abs(pos[1]))))
