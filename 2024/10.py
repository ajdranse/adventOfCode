from collections import defaultdict


DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def calc_reachable(pos, tmap):
    reach_9 = []
    if tmap[pos[0]][pos[1]] == 9:
        reach_9.append(pos)
    else:
        for d in DIRS:
            (new_r, new_c) = (pos[0] + d[0], pos[1] + d[1])
            if new_r >= 0 and new_r < len(tmap) and new_c >= 0 and new_c < len(tmap[new_r]):
                if tmap[new_r][new_c] == tmap[pos[0]][pos[1]] + 1:
                    reach_9.extend(calc_reachable((new_r, new_c), tmap))
    return reach_9

def calc_unique(pos, tmap, trail_so_far):
    cur = trail_so_far.copy()
    cur.append(pos)

    if tmap[pos[0]][pos[1]] == 9:
        return [cur]
    else:
        for d in DIRS:
            (new_r, new_c) = (pos[0] + d[0], pos[1] + d[1])

    return []

with open('10.in') as f:
    inp = [[int(y) for y in x.strip()] for x in f.readlines()]

trailheads = []
for r in range(len(inp)):
    for c in range(len(inp[r])):
        if inp[r][c] == 0:
            trailheads.append((r, c))

print(trailheads)

p1 = 0
p2 = {}
for t in trailheads:
    reachable = set(calc_reachable(t, inp))
    p1 += len(reachable)

    unique_trails = calc_reachable(t, inp)
    p2[t] = unique_trails
print('part1:', p1)

p2_val = 0
for t, endpoints in p2.items():
    uniq = defaultdict(int)
    for e in endpoints:
        uniq[e] += 1
    print(t, sum(uniq.values()))
    p2_val += sum(uniq.values())
print('part2:', p2_val)
