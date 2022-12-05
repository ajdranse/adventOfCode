import copy
import re


lines = []
with open('5.in') as f:
    lines = [x.strip() for x in f.readlines() if x.startswith('move')]

stacks = [
    ['D', 'H', 'R', 'Z', 'S', 'P', 'W', 'Q'],
    ['F', 'H', 'Q', 'W', 'R', 'B', 'V'],
    ['H', 'S', 'V', 'C'],
    ['G', 'F', 'H'],
    ['Z', 'B', 'J', 'G', 'P'],
    ['L', 'F', 'W', 'H', 'J', 'T', 'Q'],
    ['N', 'J', 'V', 'L', 'D', 'W', 'T', 'Z'],
    ['F', 'H', 'G', 'J', 'C', 'Z', 'T', 'D'],
    ['H', 'B', 'M', 'V', 'P', 'W']
]

stacks2 = copy.deepcopy(stacks)

for line in lines:
    m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
    num = int(m.group(1))
    f = int(m.group(2))
    t = int(m.group(3))

    # part 1
    for x in range(num):
        stacks[t-1].insert(0, stacks[f-1].pop(0))

    # part 2
    stacks2[t-1] = stacks2[f-1][:num] + stacks2[t-1]
    stacks2[f-1] = stacks2[f-1][num:]

print('part 1', ''.join([s[0] for s in stacks]))
print('part 2', ''.join([s[0] for s in stacks2]))
