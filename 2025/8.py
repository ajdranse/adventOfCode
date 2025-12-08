import itertools
import math
import networkx as nx

def dist(l, r):
    x = (l[0] - r[0]) ** 2
    y = (l[1] - r[1]) ** 2
    z = (l[2] - r[2]) ** 2
    return math.sqrt(x + y + z)

boxes = []
with open('8.in') as f:
    for l in f.readlines():
        l = l.strip()
        (x, y, z) = l.split(',')
        boxes.append((int(x), int(y), int(z)))

pairs = []
for (l, r) in itertools.combinations(boxes, 2):
    d = dist(l, r)
    pairs.append(((l, r), d))

pairs = sorted(pairs, key=lambda tup: tup[1])
G = nx.Graph()
cons = 0
for p in pairs:
    G.add_edge(p[0][0], p[0][1], weight=p[1])

    cons += 1
    if cons == 1000:
        p1 = 1
        i = 0
        for c in sorted(nx.connected_components(G), key=len, reverse=True)[:3]:
            p1 *= len(c)
        print(f'{p1=}')

    largest_cc = max(nx.connected_components(G), key=len)
    if len(largest_cc) == len(boxes):
        p2 = p[0][0][0] * p[0][1][0]
        print(f'{p2=}')
        break
