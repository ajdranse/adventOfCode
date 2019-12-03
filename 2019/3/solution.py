lines = []
with open('input') as f:
    lines = [x.split(',') for x in f.read().splitlines()]

def update(coord, step):
    direction = step[0]
    distance = int(step[1:])
    new_coords = []
    if direction == 'R':
        new_coords = {(coord[0] + x, coord[1], coord[2] + abs(x)) for x in range(0, distance + 1)}
        last_coord = (coord[0] + distance, coord[1], coord[2] + abs(distance))
    elif direction == 'U':
        new_coords = {(coord[0], coord[1] + x, coord[2] + abs(x)) for x in range(0, distance + 1)}
        last_coord = (coord[0], coord[1] + distance, coord[2] + abs(distance))
    elif direction == 'D':
        new_coords = {(coord[0], coord[1] - x, coord[2] + abs(x)) for x in range(0, distance + 1)}
        last_coord = (coord[0], coord[1] - distance, coord[2] + abs(distance))
    elif direction == 'L':
        new_coords = {(coord[0] - x, coord[1], coord[2] + abs(x)) for x in range(0, distance + 1)}
        last_coord = (coord[0] - distance, coord[1], coord[2] + abs(distance))
    return (new_coords, last_coord)


def find_crossings(wire1, wire2):
    wire1_nodist = {(val[0], val[1]) for val in wire1}
    wire2_nodist = {(val[0], val[1]) for val in wire2}
    return [val for val in wire1_nodist if val in wire2_nodist]


def find_smallest_crossing(wire1, wire2, by_steps):
    crossings = find_crossings(wire1, wire2)
    min_distance = 0
    min_crossing = (0, 0)
    for crossing in crossings:
        if crossing != (0,0):
            if by_steps:
                wire1_crossing = [val for val in wire1 if crossing[0] == val[0] and crossing[1] == val[1]][0]
                wire2_crossing = [val for val in wire2 if crossing[0] == val[0] and crossing[1] == val[1]][0]
                distance = wire1_crossing[2] + wire2_crossing[2]
            else:
                distance = abs(crossing[0]) + abs(crossing[1])
            if min_distance == 0 or distance < min_distance:
                min_distance = distance
                min_crossing = crossing
    return (min_crossing, min_distance)


def run(wires, by_steps):
    all_coords = []
    for wire in wires:
        last_coord = (0, 0, 0)
        coords = set()
        for step in wire:
            (new_coords, last_coord) = update(last_coord, step)
            coords.update(new_coords)
        all_coords.append(coords)
    return find_smallest_crossing(all_coords[0], all_coords[1], by_steps)


print('part 1')
(crossing, dist) = run(lines, False)
print('Min crossing is {} with distance {}'.format(crossing, dist))

print('part 2')
(crossing, dist) = run(lines, True)
print('Min crossing is {} with distance {}'.format(crossing, dist))
