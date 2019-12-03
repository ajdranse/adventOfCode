def points(wire):
    points = {}
    x = 0
    y = 0
    steps = 0
    for step in wire:
        direction = step[0]
        distance = int(step[1:])
        if direction == 'R':
            for _ in range(distance):
                x += 1
                steps += 1
                if (x, y) not in points:
                    points[(x, y)] = steps
        elif direction == 'L':
            for _ in range(distance):
                x -= 1
                steps += 1
                if (x, y) not in points:
                    points[(x, y)] = steps
        elif direction == 'U':
            for _ in range(distance):
                y += 1
                steps += 1
                if (x, y) not in points:
                    points[(x, y)] = steps
        elif direction == 'D':
            for _ in range(distance):
                y -= 1
                steps += 1
                if (x, y) not in points:
                    points[(x, y)] = steps
    return points


wires = []
with open('input') as f:
    wires = [x.split(',') for x in f.read().splitlines()]

points1 = points(wires[0])
points2 = points(wires[1])
crossings = [p for p in points1.keys() if p in points2.keys()]
print('Crossings: {}'.format(crossings))
# min_dist = None
# min_crossing = None
# for c in crossings:
#     dist = abs(c[0]) + abs(c[1])
#     if min_dist is None or dist < min_dist:
#         min_dist = dist
#         min_crossing = c
#         print('New min, crossing {} has distance {}'.format(c, dist))
distances = [abs(p[0]) + abs(p[1]) for p in crossings]
min_dist = min(distances)
print('part 1: {}'.format(min_dist))

steps = [points1[p] + points2[p] for p in crossings]
min_steps = min(steps)
print('part 2: {}'.format(min_steps))
