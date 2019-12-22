from intcode import IntCode
from queue import Queue


def from_ascii(vals):
    out = ''
    for c in vals:
        try:
            out += str(chr(c))
        except ValueError:
            print('Not ascii: {}'.format(c))
    return out


def to_ascii(instr):
    out = []
    for c in instr:
        out.append(ord(c))
    out.append(10)
    print(instr, out)
    return out


def part1(inq):
    # true if there is a hole at 1
    for v in to_ascii('NOT A T'):
        inq.put(v)
    # true if there is a hole at 2
    for v in to_ascii('NOT B J'):
        inq.put(v)
    # true if htere is a hole at 1 or 2
    for v in to_ascii('OR T J'):
        inq.put(v)
    # true if there is a hole at 3
    for v in to_ascii('NOT C T'):
        inq.put(v)
    # true if there is a hole at 1, 2, or 3
    for v in to_ascii('OR T J'):
        inq.put(v)
    # true if there is ground at 4
    for v in to_ascii('AND D J'):
        inq.put(v)


def part2(inq):
    # J will be set to true if there is a hole at 1, 2, or 3 and ground at 4
    # we want to NOT jump if there is a hole at 5 or 8 (E or H)
    # so E or H must be true (ground)
    # reset T to True (D must be true)
    for v in to_ascii('OR D T'):
        inq.put(v)
    # put E in T
    for v in to_ascii('AND E T'):
        inq.put(v)
    # E or H is true
    for v in to_ascii('OR H T'):
        inq.put(v)
    # put result in jump
    for v in to_ascii('AND T J'):
        inq.put(v)


print('part1')
with open('21.in') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    inq = Queue()
    outq = Queue()
    t = IntCode(memory.copy(), inq, outq)
    t.start()
    vals = []
    while not outq.empty():
        vals.append(outq.get())
    print(from_ascii(vals))
    part1(inq)
    # go
    for v in to_ascii('WALK'):
        inq.put(v)
    t.join()
    while not outq.empty():
        vals.append(outq.get())
    print(from_ascii(vals))

print('part2')
with open('21.in') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    inq = Queue()
    outq = Queue()
    t = IntCode(memory.copy(), inq, outq)
    t.start()
    vals = []
    while not outq.empty():
        vals.append(outq.get())
    print(from_ascii(vals))
    # jump if there is a hole at 1, 2, or 3, and ground at 4
    part1(inq)
    # don't jump if there is a hole at 5 or 8 (i.e. we can't walk a step or jump once more)
    part2(inq)
    # go
    for v in to_ascii('RUN'):
        inq.put(v)
    t.join()
    while not outq.empty():
        vals.append(outq.get())
    print(from_ascii(vals))
