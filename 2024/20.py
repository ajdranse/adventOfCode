import networkx

from collections import defaultdict
from itertools import combinations

def print_saved(p):
    saved = defaultdict(int)
    for _, _, s in p:
        saved[s] += 1
    saved = dict(sorted(saved.items(), key=lambda x: x[0]))
    for s, c in saved.items():
        print(s, c)

def safe(m, y, x):
    y_ok = 1 <= y < len(m) - 1
    x_ok = 1 <= x < len(m) - 1
    chars_ok = m[y][x] in '.SE'
    return y_ok and x_ok and chars_ok

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_pairs(G, path, picos):
    pairs = []
    i = 0
    combos = list(combinations(path, 2))
    print(f'{len(combos)=}')
    for n, n2 in combos:
        if i % 1000 == 0:
            print(f'{i}...')
        dist = manhattan(n, n2)
        if dist <= picos:
            saved = networkx.shortest_path(G, n, n2)
            if len(saved) - dist >= 100:
                pairs.append((n, n2, len(saved) - dist - 1))
        i += 1
    return pairs

with open('20.in') as f:
    inp = [x.strip() for x in f.readlines()]

s = e = None
G = networkx.Graph()
# add nodes
for y in range(len(inp)):
    for x in range(len(inp[y])):
        if inp[y][x] == 'S':
            s = (y, x)
        if inp[y][x] == 'E':
            e = (y, x)

        if inp[y][x] in '.SE':
            G.add_node((y, x))

# add edges
for y in range(len(inp)):
    for x in range(len(inp[y])):
        if inp[y][x] in '.SE1':
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                if safe(inp, ny, nx):
                    G.add_edge((y, x), (ny, nx))

print(f'Start: {s}')
print(f'End: {e}')
soln = networkx.shortest_path(G, source=s, target=e)

part1 = get_pairs(G, soln, 2)
# print_saved(part1)
print('part1:', len(part1))
part2 = get_pairs(G, soln, 20)
# print_saved(part2)
print('part2:', len(part2))
