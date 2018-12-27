import networkx

depth = 4080
target = (14, 785)
#depth = 510
#target = (10, 10)

rocky, wet, narrow = 0, 1, 2
torch, climbing_gear, none = 0, 1, 2

items = {
    rocky: (torch, climbing_gear),
    wet: (climbing_gear, none),
    narrow: (torch, none)
}

can_use_in = {
    torch: (rocky, narrow),
    climbing_gear: (rocky, wet),
    none: (wet, narrow)
}

xmax = target[0] + 100
ymax = target[1] + 100
erosion_levels = [[0 for x in xrange(0, xmax + 1)] for y in xrange(0, ymax + 1)]
types = [[0 for x in xrange(0, xmax + 1)] for y in xrange(0, ymax + 1)]
for y in xrange(0, ymax + 1):
    for x in xrange(0, xmax + 1):
        geologic_index = 0
        if (x, y) == (0, 0) or (x, y) == target:
            pass
        elif y == 0:
            geologic_index = x * 16807
        elif x == 0:
            geologic_index = y * 48271
        else:
            geologic_index = erosion_levels[y][x-1] * erosion_levels[y-1][x]
        erosion_levels[y][x] = (geologic_index + depth) % 20183
        types[y][x] = (erosion_levels[y][x] % 3)

risk_sum = 0
for y in xrange(0, target[1] + 1):
    for x in xrange(0, target[0] + 1):
        risk_sum += types[y][x]
print(risk_sum)

graph = networkx.Graph()
for y in xrange(0, ymax):
    for x in xrange(0, xmax):
        can_use = items[types[y][x]]
        # add change-gear edge
        graph.add_edge((x, y, can_use[0]), (x, y, can_use[1]), weight=7)

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            newx, newy = x+dx, y+dy
            if 0 <= newx <= xmax and 0 <= newy <= ymax:
                new_can_use = items[types[newy][newx]]
                for inter in set(can_use).intersection(set(new_can_use)):
                    graph.add_edge((x, y, inter), (newx, newy, inter), weight=1)

print(networkx.dijkstra_path_length(graph, (0, 0, torch), (target[0], target[1], torch)))
