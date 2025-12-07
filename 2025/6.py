import math

from collections import defaultdict

probs = []
with open('6.in') as f:
    for l in f.readlines():
        l = l.strip()
        for idx, c in enumerate(l.split()):
            if len(probs) < idx+1:
                probs.append([])
            probs[idx].append(int(c) if c != '*' and c != '+' else c)

p1 = 0
for p in probs:
    op = p[-1]
    vals = p[:len(p)-1]
    if op == '*':
        p1 += math.prod(vals)
    elif op == '+':
        p1 += sum(vals)
print(f'{p1=}')

with open('6.in') as f:
    lines = [x[:-1] for x in f.readlines()]

problems = []
skip = False
op = ''
prob = []
for x in range(len(lines[0]) - 1, -1, -1):
    if skip:
        skip = False
        problems.append((op, prob))
        op = ''
        prob = []
        continue

    p = ''
    op = ''
    for y in range(len(lines)):# - 1, 0, -1):
        c = lines[y][x]
        if c == '*' or c == '+':
            skip = True
            op = c
        else:
            p += c
    p = p.strip()
    prob.append(int(p))
problems.append((op, prob))

p2 = 0
for p in problems:
    op = p[0]
    vals = p[1]
    if op == '*':
        p2 += math.prod(vals)
    elif op == '+':
        p2 += sum(vals)
print(f'{p2=}')
