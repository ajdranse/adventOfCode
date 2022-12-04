lines = []
with open('4.in') as f:
    lines = [x.strip() for x in f.readlines()]
contained = 0
overlap = 0

for l in lines:
    one, two = l.split(',')
    os, oe = one.split('-')
    r = set([x for x in range(int(os), int(oe) + 1)])
    ts, te = two.split('-')
    r2 = set([x for x in range(int(ts), int(te) + 1)])

    o = r & r2

    if o == r or o == r2:
        contained += 1
    if len(o) > 0:
        overlap += 1

print('part 1', contained)
print('part 2', overlap)
