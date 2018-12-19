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

    def execute(self, ip, program, registers):
        while registers[ip] < len(program):
            # main loop of program adds all the divisors of the number in registers[4] 
            # together and puts that into registers[0]
            if registers[ip] == 2:
                divide = registers[4]
                for i in xrange(1, divide+1):
                    if divide % i == 0:
                        registers[0] += i
                break
            instr = program[registers[ip]]
            c = instr.split()
            op = c[0]
            a = int(c[1])
            b = int(c[2])
            c = int(c[3])
            method = getattr(computer, op)
            method(registers, a, b, c)
            registers[ip] += 1

        print("Done, registers are: {}".format(registers))


lines = []
with open('input') as f:
    for line in f:
        line = line.rstrip()
        lines.append(line)

ip = None
instructions = []
for line in lines:
    if line.startswith("#ip"):
        ip = int(line.split(' ')[1])
    else:
        instructions.append(line)

computer = Computer()
# part 1
computer.execute(ip, instructions, [0, 0, 0, 0, 0, 0])
# part 2
computer.execute(ip, instructions, [1, 0, 0, 0, 0, 0])
