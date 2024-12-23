import networkx
import matplotlib.pyplot as plt

from itertools import combinations
from collections import defaultdict


with open('23.in') as f:
    inp = [x.strip() for x in f.readlines()]

G = networkx.Graph()
for l in inp:
    f, t = l.split('-')
    G.add_edge(f, t)

all_connected = set()
largest_set = set()
for n in G:
    for n2 in networkx.neighbors(G, n):
        common_neighbors = networkx.common_neighbors(G, n, n2)
        if len(common_neighbors) > 0:
            for n3 in common_neighbors:
                inter = tuple(sorted((n, n2, n3)))
                if inter not in all_connected and n.startswith('t'):
                    all_connected.add(inter)
        common_neighbors.add(n)
        common_neighbors.add(n2)
        H = G.subgraph(common_neighbors)
        if not any(len(d) != len(H) - 1 for d in H.adj.values()) and len(common_neighbors) > len(largest_set):
            largest_set = common_neighbors

print('part1:', len(all_connected))
print('part2:', ','.join(sorted(largest_set)))
