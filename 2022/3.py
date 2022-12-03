inp = '3.in'
lines = []
with open(inp) as f:
    lines = [x.strip() for x in f.readlines()]

prio1 = 0
prio2 = 0
for i, l in enumerate(lines):
    left = l[:int(len(l)/2)]
    right = l[int(len(l)/2):]
    for c in left:
        if c in right:
            if ord(c) < 97:
                prio1 += ord(c) - 38
            else:
                prio1 += ord(c) - 96
            break

    if i % 3 == 0:
        one = lines[i]
        two = lines[i+1]
        three = lines[i+2]
        for c in one:
            if c in two and c in three:
                if ord(c) < 97:
                    prio2 += ord(c) - 38
                else:
                    prio2 += ord(c) - 96
                break

print('part 1', prio1)
print('part 2', prio2)
