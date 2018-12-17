import copy
import re

from sets import Set


class Computer:
    def addr(self, r, a, b, c):
        r[c] = r[a] + r[b]


    def addi(self, r, a, b, c):
        r[c] = r[a] + b


    def mulr(self, r, a, b, c):
        r[c] = r[a] * r[b]


    def muli(self, r, a, b, c):
        r[c] = r[a] * b


    def banr(self, r, a, b, c):
        r[c] = r[a] & r[b]


    def bani(self, r, a, b, c):
        r[c] = r[a] & b


    def borr(self, r, a, b, c):
        r[c] = r[a] | r[b]


    def bori(self, r, a, b, c):
        r[c] = r[a] | b


    def setr(self, r, a, b, c):
        r[c] = r[a]


    def seti(self, r, a, b, c):
        r[c] = a


    def gtir(self, r, a, b, c):
        r[c] = 1 if a > r[b] else 0


    def gtri(self, r, a, b, c):
        r[c] = 1 if r[a] > b else 0


    def gtrr(self, r, a, b, c):
        r[c] = 1 if r[a] > r[b] else 0


    def eqir(self, r, a, b, c):
        r[c] = 1 if a == r[b] else 0


    def eqri(self, r, a, b, c):
        r[c] = 1 if r[a] == b else 0


    def eqrr(self, r, a, b, c):
        r[c] = 1 if r[a] == r[b] else 0


    def __init__(self):
        self.functions = [self.addr, self.addi, self.mulr, self.muli, self.banr, self.bani, self.borr, self.bori, self.setr, self.seti, self.gtir, self.gtri, self.gtrr, self.eqir, self.eqri, self.eqrr]

lines = []
with open('input') as f:
    for line in f:
        line = line.rstrip()
        lines.append(line)

pattern = re.compile(r'.*\[(\d), (\d), (\d), (\d)\]')

possible = {}
many_matches = 0
i = 0
code = []
computer = Computer()
while i < len(lines):
    line = lines[i]
    if line.startswith("Before:"):
        line2 = lines[i+1]
        line3 = lines[i+2]
        before = [int(x) for x in list(re.match(pattern, line).groups())]
        opcode = [int(x) for x in line2.split()]
        after = [int(x) for x in list(re.match(pattern, line3).groups())]
        i = i+3

        matches = 0
        cur_possible = []
        for func in computer.functions:
            registers = copy.copy(before)
            func(registers, opcode[1], opcode[2], opcode[3])
            if registers == after:
                cur_possible.append(func.__name__)
                matches += 1

        if opcode[0] in possible:
            possible[opcode[0]] &= Set(cur_possible)
        else:
            possible[opcode[0]] = Set(cur_possible)

        if matches >= 3:
            many_matches += 1
    elif len(line) > 0:
        code.append(line)

    i += 1

print("part 1: {} opcodes have 3+ matches".format(many_matches))

opcodes = {}
max_len = max([len(x) for x in possible.itervalues()])
while max_len > 0:
    to_remove = []
    for i, p in possible.iteritems():
        if len(p) == 1:
            val = p.pop()
            to_remove.append(val)
            opcodes[i] = val

    if len(to_remove) > 0:
        for i in possible.iterkeys():
            for r in to_remove:
                possible[i].discard(r)

    max_len = max([len(x) for x in possible.itervalues()])
print(opcodes)

registers = [0, 0, 0, 0]
for c in code:
    c = c.split()
    opcode = int(c[0])
    a = int(c[1])
    b = int(c[2])
    c = int(c[3])

    method = getattr(computer, opcodes[opcode])
    method(registers, a, b, c)

print(registers)
