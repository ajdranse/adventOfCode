import copy

lines = []
with open('3.in') as f:
    lines = f.read().splitlines()

# lines = [ '00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010', ]

# gamma rate = most common bit of all positions
# epsilon rate is least common

g = ''
e = ''
for i in range(len(lines[0])):
    s = sum([int(w[i]) for w in lines])
    # 1 is most common
    if s > len(lines) / 2:
        g += '1'
        e += '0'
    # 0 is most common
    else:
        g += '0'
        e += '1'

print(f'part 1: {int(g, 2)* int(e, 2)}')

# oxy rating: most common in that position, keep lines with only that bit
# co2 rating: least common

oxy = copy.copy(lines)
idx = 0
while len(oxy) > 1:
    s = sum([int(w[idx]) for w in oxy])
    # 1 most common or equal
    if s >= len(oxy) / 2:
        oxy = [x for x in oxy if x[idx] == '1']
    # 0 most common
    else:
        oxy = [x for x in oxy if x[idx] == '0']
    idx += 1
oxy = oxy[0]

co2 = copy.copy(lines)
idx = 0
while len(co2) > 1:
    s = sum([int(w[idx]) for w in co2])
    # 1 most common or equal
    if s >= len(co2) / 2:
        co2 = [x for x in co2 if x[idx] == '0']
    # 0 most common
    else:
        co2 = [x for x in co2 if x[idx] == '1']
    idx += 1
co2 = co2[0]
print(f'part 2: {int(oxy, 2) * int(co2, 2)}')
