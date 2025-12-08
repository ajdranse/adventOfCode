from collections import defaultdict

with open('7.in') as f:
    lines = [x.strip() for x in f.readlines()]

beams = {lines[0].index('S'): 1}
rows = []
for idx in range(1, len(lines)):
    if '^' not in lines[idx]:
        continue

    cur = []
    for idx, c in enumerate(lines[idx]):
        if c == '^':
            cur.append(idx)
    rows.append(cur)

p1 = 0
for r in rows:
    next_beams = defaultdict(int)
    for x, n in beams.items():
        if x in r:
            p1 += 1
            next_beams[x-1] += n
            next_beams[x+1] += n
        else:
            next_beams[x] += n
    beams = next_beams
print(f'{p1=}')
print(f'p2={sum([beams[i] for i in beams])}')
