import re

fields = {}
my_ticket = []
others = []

with open('16.in') as f:
# with open('16.test') as f:
# with open('16.test2') as f:
    next_mine = False
    next_others = False
    for line in f:
        line = line.rstrip()
        if ' or ' in line:
            # key: range1 or range2
            m = re.search('(.+): (\d+)-(\d+) or (\d+)-(\d+)', line)
            key = m.group(1)
            range1_low = int(m.group(2))
            range1_high = int(m.group(3))
            range2_low = int(m.group(4))
            range2_high = int(m.group(5))
            fields[key] = [x for x in range(range1_low, range2_high + 1) if range1_low <= x <= range1_high or range2_low <= x <= range2_high]
        elif line == 'your ticket:':
            next_mine = True
        elif next_mine:
            next_mine = False
            my_ticket = [int(x) for x in line.split(',')]
        elif line == 'nearby tickets:':
            next_others = True
        elif next_others:
            others.append([int(x) for x in line.split(',')])

all_valid = sorted([item for sublist in fields.values() for item in sublist])
invalid_fields = []
valid_others = []
for o in others:
    invalid = False
    for v in o:
        if v not in all_valid:
            invalid_fields.append(v)
            invalid = True
    if not invalid:
        valid_others.append(o)

print('part1: {}'.format(sum(invalid_fields)))

by_pos = {}
for o in valid_others:
    for idx, f in enumerate(o):
        if idx not in by_pos:
            by_pos[idx] = [f]
        else:
            by_pos[idx].append(f)

decoded = {}
for pos, vs in by_pos.items():
    for k, v in fields.items():
        if all(value in v for value in vs):
            if pos not in decoded:
                decoded[pos] = [k]
            else:
                decoded[pos].append(k)
while not(all(len(v) == 1 for v in decoded.values())):
    len_one = {key:val[0] for key, val in decoded.items() if len(val) == 1}
    for k, v in decoded.items():
        if k not in len_one:
            newvals = [val for val in v if val not in len_one.values()]
            decoded[k] = newvals
decoded = {k: v[0] for k, v in decoded.items()}

prod = 1
for idx, v in enumerate(my_ticket):
    if decoded[idx].startswith('departure'):
        prod *= v
print('part2: {}'.format(prod))
