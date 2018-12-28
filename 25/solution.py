import re
import networkx

def dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + abs(pos1[2] - pos2[2]) + abs(pos1[3] - pos2[3])

pattern = re.compile(r'(-?\d+),(-?\d+),(-?\d+),(-?\d+)')

points = []
with open('input') as f:
    for line in f:
        line = line.rstrip()
        m = re.match(pattern, line)
        x = int(m.group(1))
        y = int(m.group(2))
        z = int(m.group(3))
        w = int(m.group(4))
        points.append((x, y, z, w))

constellations = networkx.Graph()
for i, p in enumerate(points):
    for j, pp in enumerate(points):
        if dist(p, pp) <= 3:
            constellations.add_edge(p, pp)
print("part 1: {}".format(networkx.number_connected_components(constellations)))
