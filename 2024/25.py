from collections import defaultdict

from itertools import combinations

def calc(rows):
    lock = False
    key = False
    if rows[0] == '#####' and rows[-1] == '.....':
        # lock mode
        lock = True
    elif rows[0] == '.....' and rows[-1] == '#####':
        # key mode
        key = True

    cols = [0, 0, 0, 0, 0]
    for r in rows[1:-1]:
        for idx, c in enumerate(r):
            if c == '#':
                cols[idx] += 1
    return lock, cols

with open('25.in') as f:
    inp = [x.strip() for x in f.readlines()]

rows = []
m = defaultdict(list)
for l in inp:
    if l == '':
        t, vals = calc(rows)
        rows = []
        m[t].append(vals)
    else:
        rows.append(l)
locks = m[True]
keys = m[False]

fits = 0
for l in locks:
    for k in keys:
        for c in range(len(l)):
            if l[c] + k[c] > 5:
                break
        else:
            fits += 1
print(fits)
