import re
import operator

def manhattan_distance(bot, other):
    pos, r = bot
    opos, _ = other
    dist = abs(pos[0] - opos[0]) + abs(pos[1] - opos[1]) + abs(pos[2] - opos[2])
    range = False
    if dist <= r:
        range = True
    return dist, range

bots = []
pattern = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)')
with open('input') as f:
    for line in f:
        line = line.rstrip()
        m = re.match(pattern, line)
        x = m.group(1)
        y = m.group(2)
        z = m.group(3)
        r = m.group(4)
        bots.append(((int(x), int(y), int(z)), int(r)))

strongest = max(bots, key=lambda x: x[1])

num_in_range = 0
for bot in bots:
    dist, in_range = manhattan_distance(strongest, bot)
    if in_range:
        num_in_range += 1

print("part 1: {}".format(num_in_range))

from z3 import *
def zabs(v):
    return If(v >= 0, v, -v)

x, y, z = Int('x'), Int('y'), Int('z')
in_ranges = [ Int('in_range_' + str(i)) for i in range(len(bots)) ]
range_count = Int('sum')
o = Optimize()
for i in range(len(bots)):
    (nx, ny, nz), nr = bots[i]
    o.add(in_ranges[i] == If(zabs(x - nx) + zabs(y - ny) + zabs(z - nz) <= nr, 1, 0))
o.add(range_count == sum(in_ranges))
dist_from_zero = Int('dist')
o.add(dist_from_zero == zabs(x) + zabs(y) + zabs(z))
h1 = o.maximize(range_count)
h2 = o.minimize(dist_from_zero)
print(o.check())
print("part 2: {} {}".format(o.lower(h2), o.upper(h2)))
