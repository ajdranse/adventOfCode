from collections import defaultdict


DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def calc_reachable(pos, tmap):
    (r, c) = pos
    if tmap[r][c] == 9:
        return [pos]
    else:
        trails = []
        for (dr, dc) in DIRS:
            (new_r, new_c) = (r + dr, c + dc)
            if new_r >= 0 and new_r < len(tmap) and new_c >= 0 and new_c < len(tmap[new_r]):
                if tmap[new_r][new_c] == tmap[r][c] + 1:
                    trails.extend(calc_reachable((new_r, new_c), tmap))
        return trails

with open('10.in') as f:
    inp = [[int(y) for y in x.strip()] for x in f.readlines()]

trailheads = defaultdict(lambda: defaultdict(int))
for r in range(len(inp)):
    for c in range(len(inp[r])):
        if inp[r][c] == 0:
            for t in calc_reachable((r, c), inp):
                trailheads[(r, c)][t] += 1

p1 = sum([len(t.keys()) for t in trailheads.values()])
print('part1:', p1)
p2 = sum([sum(t.values()) for t in trailheads.values()])
print('part2:', p2)
