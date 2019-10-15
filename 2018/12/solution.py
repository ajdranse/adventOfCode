import collections
import re
import sys

def prune(state):
    first_plant = state.index(1)
    last_plant = len(state) - 1 - state[::-1].index(1)
    return (state[first_plant:last_plant+1], first_plant)

def printstate(state):
    string = ""
    for s in state:
        if s == 1:
            string += "#"
        else:
            string += "."

    return string

def grow(plants_in, patterns):
    first = min(plants_in)
    last = max(plants_in)

    new_generation = set()
    for i in xrange(first - 3, last + 4):
        cur_pattern = ''.join('#' if i + offset in plants_in else '.' for offset in [-2, -1, 0, 1, 2])
        if cur_pattern in patterns:
            new_generation.add(i)
    return new_generation

initial_pattern = re.compile(r'initial state: (.*)')
initial_state = ''
patterns = set()
with open('input') as f:
    for line in f:
        line = line.rstrip()
        m = re.match(initial_pattern, line)
        if m:
            initial_state = m.group(1)
        else:
            split = line.split(' => ')
            if len(split) > 1 and split[1] == '#':
                patterns.add(split[0])

print("patterns: {}".format(patterns))
plants_in = set(i for i, c in enumerate(initial_state) if c == '#')
print("initially, plants in: {}".format(plants_in))

for i in xrange(20):
    plants_in = grow(plants_in, patterns)

print("part 1: {}".format(sum(plants_in)))

plants_in = set(i for i, c in enumerate(initial_state) if c == '#')
s = sum(plants_in)
for i in xrange(1, 160):
    plants_in = grow(plants_in, patterns)
    cur_sum = sum(plants_in)
    diff = cur_sum - s
    s = cur_sum

# every generation after adds 42 from experimentation
gens_left = 50000000000 - 159
print("part 2: {}".format(s + (gens_left * 42)))
