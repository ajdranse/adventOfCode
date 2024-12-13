import re

from itertools import combinations
from z3 import *


with open('13.in') as f:
    inp = [x.strip() for x in f.readlines()]

# 3 to push A
# 1 to push B

# moves right (x) and forward (y)

machines = []
a = None
b = None
prize = None
for l in inp:
    if 'A' in l:
        # a button
        a = list(map(int, re.search(r'X\+(\d+), Y\+(\d+)', l).groups()))
    elif 'B' in l:
        b = list(map(int, re.search(r'X\+(\d+), Y\+(\d+)', l).groups()))
        # b button
    elif 'Prize' in l:
        prize = list(map(int, re.search(r'X=(\d+), Y=(\d+)', l).groups()))
        # prize location
    else:
        machines.append((a, b, prize))
        a = b = prize = None
machines.append((a, b, prize))
a = b = prize = None

def solve(part2 = False):
    wins = []
    for m in machines:
        Ax = m[0][0]
        Ay = m[0][1]
        Bx = m[1][0]
        By = m[1][1]
        X = m[2][0]
        Y = m[2][1]
        if part2:
            X += 10000000000000
            Y += 10000000000000

        a = Int('a')
        b = Int('b')
        cost = Int('cost')
        opt = Optimize()
        opt.add(Ax * a + Bx * b == X)
        opt.add(Ay * a + By * b == Y)
        opt.add(cost == 3*a + b)
        h = opt.minimize(cost)
        opt.check()
        opt.lower(h)
        mod = opt.model()
        if mod[cost] is not None:
            wins.append(mod)
    return sum([w[cost].as_long() for w in wins])

print('part1:', solve())
print('part2:', solve(True))
