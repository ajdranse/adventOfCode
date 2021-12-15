import networkx as nx

def solve(lines, part2):
    G = nx.DiGraph()

    its = 1
    if part2:
        its = 5

    y_it = 0
    while y_it < its:
        y = 0
        for l in lines:
            x_it = 0
            while x_it < its:
                x = 0
                for c in l:
                    x_coord = x + (x_it * len(lines[0]))
                    y_coord = y + (y_it * len(lines))
                    G.add_node((x_coord, y_coord))

                    cost = (int(c) + x_it + y_it - 1) % 9 + 1

                    if x_coord > 0:
                        G.add_edge((x_coord-1, y_coord), (x_coord, y_coord), weight=cost)
                    if x_coord < its * len(lines[0]):
                        G.add_edge((x_coord+1, y_coord), (x_coord, y_coord), weight=cost)
                    if y_coord > 0:
                        G.add_edge((x_coord, y_coord-1), (x_coord, y_coord), weight=cost)
                    if y_coord < its * len(lines):
                        G.add_edge((x_coord, y_coord+1), (x_coord, y_coord), weight=cost)
                    x += 1
                x_it +=1
            y += 1
        y_it += 1

    start = (0, 0)
    end = (its*len(lines)-1, its*len(lines[0])-1)

    path = nx.shortest_path(G, source=start, target=end, weight='weight')
    return nx.classes.function.path_weight(G, path, weight='weight')

with open('15.in') as f:
    lines = f.read().splitlines()

print(f'part1: {solve(lines, False)}')
print(f'part2: {solve(lines, True)}')
