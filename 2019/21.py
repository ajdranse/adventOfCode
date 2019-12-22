from intcode import print_grid, IntCode
from queue import Queue


def from_ascii(vals):
    try :
        out = ''
        for c in vals:
            out += str(chr(c))
        return out
    except ValueError:
        print('Not ascii: {}'.format(vals))

def to_ascii(instr):
    out = []
    for c in instr:
        out.append(ord(c))
    out.append(10)
    print(instr, out)
    return out


print('part1')
with open('21.in') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    inq = Queue()
    outq = Queue()
    t = IntCode(memory.copy(), inq, outq)
    t.start()
# part 1
# jump if there is ground at 4 and a hole at 1 2 or 3
# NOT A T # T is true if there is a hole at 1
# NOT B J # J is true if there is a hole at 2
# OR T J # J is true if there is a hole at 1 or 2
# NOT C T # J is true if there is a hole at 3
# OR T J # T is true if htere is a hole at 1 2 or 3
# AND D J # J is true if there is ground at 4 and a hole at 1 2 or 3
    vals = []
    while not outq.empty():
        vals.append(outq.get())
    print(from_ascii(vals))

    for v in to_ascii('NOT A T'):
        inq.put(v)
    for v in to_ascii('NOT B J'):
        inq.put(v)
    for v in to_ascii('OR T J'):
        inq.put(v)
    for v in to_ascii('NOT C T'):
        inq.put(v)
    for v in to_ascii('OR T J'):
        inq.put(v)
    for v in to_ascii('AND D J'):
        inq.put(v)
    for v in to_ascii('RUN'):
        inq.put(v)
    t.join()
    while not outq.empty():
        vals.append(outq.get())
    print(from_ascii(vals))
