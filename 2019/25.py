from intcode import IntCode
from queue import Queue
import time

# Movement via north, south, east, or west.
# To take an item the droid sees in the environment, use the command take <name of item>. For example, if the droid reports seeing a red ball, you can pick it up with take red ball.
# To drop an item the droid is carrying, use the command drop <name of item>. For example, if the droid is carrying a green ball, you can drop it with drop green ball.
# To get a list of all of the items the droid is currently carrying, use the command inv (for "inventory").


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


def get_program():
    with open('25.in') as f:
        memory = [int(x.strip()) for x in f.read().split(',')]
    return memory


def print_output(outq):
    vals = []
    while not outq.empty():
        vals.append(outq.get())
    print(from_ascii(vals))

memory = get_program()
inq = Queue()
outq = Queue()
t = IntCode(memory.copy(), inq, outq)
t.start()
inp = ''
while inp != 'quit':
    time.sleep(0.25)
    print_output(outq)
    inp = input('> ')
    for c in to_ascii(inp):
        inq.put(c)
    # op = t.tick()
    # if op == 3:
    #     inp = input('> ')
    #     for c in to_ascii(inp):
    #         inq.put(c)
    # elif op == 4:
    #     print_output(outq)
