import networkx as nx
from collections import defaultdict, deque


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def build_graph(grid, portals, start, d):
    directions = [1, 2, 3, 4]
    DX = {1: 1, 2: -1, 3: 0, 4: 0}
    DY = {1: 0, 2: 0,  3: 1, 4: -1}
    print(d)
    g = nx.Graph()
    todo = deque([start])
    seen = set()
    while todo:
        cur = todo.popleft()
        if cur in seen:
            continue
        seen.add(cur)
        for i in directions:
            test_pos = (cur[0] + DX[i], cur[1] + DY[i])
            if test_pos in seen:
                continue
            if grid[test_pos] == '.':
                # print('adding edge 1', cur + (d, ), test_pos + (d, ))
                g.add_edge(cur + (d, ), test_pos + (d, ))
                todo.append(test_pos)
        if cur + (0, ) in portals:
            maps_to = portals[cur + (0,)]
            # print('adding edge 2', cur + (d, ), (maps_to[0], maps_to[1], d+1))
            g.add_edge(cur + (d, ), (maps_to[0], maps_to[1], d+1))
            todo.append((maps_to[0], maps_to[1]))
        elif cur + (1, ) in portals and d > 0:
            maps_to = portals[cur + (1,)]
            # print('adding edge 3', cur + (d, ), (maps_to[0], maps_to[1], d-1))
            g.add_edge(cur + (d, ), (maps_to[0], maps_to[1], d-1))
            todo.append((maps_to[0], maps_to[1]))
    return g


def build_portals(grid):
    portals = defaultdict(list)
    min_y = min(grid, key=lambda g: g[1])[1]
    max_y = max(grid, key=lambda g: g[1])[1]
    min_x = min(grid, key=lambda g: g[0])[0]
    max_x = max(grid, key=lambda g: g[0])[0]
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            c = grid[(x, y)]
            if c == '.':
                up1 = grid[(x, y-1)]
                up2 = grid[(x, y-2)]
                if up1 == 'A' and up2 == 'A':
                    start_pos = (x, y, 0)
                elif up1 == 'Z' and up2 == 'Z':
                    end_pos = (x, y, 0)
                elif up1 in LETTERS and up2 in LETTERS:
                    portals[up2 + up1].append((x, y))

                left1 = grid[(x-1, y)]
                left2 = grid[(x-2, y)]
                if left1 == 'A' and left2 == 'A':
                    start_pos = (x, y, 0)
                elif left1 == 'Z' and left2 == 'Z':
                    end_pos = (x, y, 0)
                elif left1 in LETTERS and left2 in LETTERS:
                    portals[left2 + left1].append((x, y))

                right1 = grid[(x+1, y)]
                right2 = grid[(x+2, y)]
                if right1 == 'A' and right2 == 'A':
                    start_pos = (x, y, 0)
                elif right1 == 'Z' and right2 == 'Z':
                    end_pos = (x, y, 0)
                elif right1 in LETTERS and right2 in LETTERS:
                    portals[right1 + right2].append((x, y))

                down1 = grid[(x, y+1)]
                down2 = grid[(x, y+2)]
                if down1 == 'A' and down2 == 'A':
                    start_pos = (x, y, 0)
                elif down1 == 'Z' and down2 == 'Z':
                    end_pos = (x, y, 0)
                elif down1 in LETTERS and down2 in LETTERS:
                    portals[down1 + down2].append((x, y))
    direct_portals = {}
    for p in portals.values():
        if p[0][0] == 2 or p[0][1] == 2 or p[0][0] == max_x - 2 or p[0][1] == max_y - 2:
            # outer portal
            direct_portals[(p[0][0], p[0][1], 1)] = (p[1][0], p[1][1], 0)
            direct_portals[(p[1][0], p[1][1], 0)] = (p[0][0], p[0][1], 1)
        else:
            # inner portal
            direct_portals[(p[0][0], p[0][1], 0)] = (p[1][0], p[1][1], 1)
            direct_portals[(p[1][0], p[1][1], 1)] = (p[0][0], p[0][1], 0)
    return direct_portals, start_pos, end_pos


def run(filename):
    grid = {}
    portals = {}
    lines = []
    start_pos = None
    end_pos = None
    with open(filename) as f:
        lines = [x.strip('\n') for x in f.readlines()]
        y = 0
        for line in lines:
            x = 0
            for c in line:
                grid[(x, y)] = c
                x += 1
            y += 1

    print('building portals')
    portals, start_pos, end_pos = build_portals(grid)
    print('building graph')
    graph = nx.Graph()
    for d in range(2):
        g = build_graph(grid, portals, (start_pos[0], start_pos[1]), d)
        graph = nx.compose(graph, g)
    print('going from {} to {}'.format(start_pos, end_pos))
    found = False
    depth = 1
    while depth < 100 and not found:
        try:
            p = nx.shortest_path(graph, start_pos, end_pos)
            found = True
            print(len(p) - 1)
            # print(list(p))
        except Exception:
            depth += 1
            g = build_graph(grid, portals, (start_pos[0], start_pos[1]), depth)
            graph = nx.compose(graph, g)

# run('20.test')
# run('20.test.2')
# run('20.test.3')
run('20.in')
