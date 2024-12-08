import itertools
from collections import defaultdict

def step(a, b):
    return (b[0] - a[0], b[1] - a[1])

with open('8.in') as f:
    inp = [x.strip() for x in f.readlines()]

nodes = defaultdict(list)
for r in range(len(inp)):
    for c in range(len(inp[r])):
        if inp[r][c] != '.':
            nodes[inp[r][c]].append((r, c))

p1_antinodes = set()
p2_antinodes = set()
for freq, antennas in nodes.items():
    for pair in itertools.combinations(antennas, 2):
        s = step(pair[0], pair[1])
        p1_antinodes.add((pair[1][0] + s[0], pair[1][1] + s[1]))
        p1_antinodes.add((pair[0][0] - s[0], pair[0][1] - s[1]))

        a = pair[1]
        while a[0] >= 0 and a[0] < len(inp) and a[1] >= 0 and a[1] < len(inp[0]):
            p2_antinodes.add(a)
            a = (a[0] + s[0], a[1] + s[1])

        a = pair[0]
        while a[0] >= 0 and a[0] < len(inp) and a[1] >= 0 and a[1] < len(inp[0]):
            p2_antinodes.add(a)
            a = (a[0] - s[0], a[1] - s[1])

part1 = 0
for a in p1_antinodes:
    if a[0] >= 0 and a[0] < len(inp) and a[1] >= 0 and a[1] < len(inp[0]):
        part1 += 1
print(f'{part1=}')

part2 = len(p2_antinodes)
print(f'{part2=}')
