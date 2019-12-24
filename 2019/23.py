from intcode import IntCode
from queue import Queue


def get_program():
    with open('23.in') as f:
        memory = [int(x.strip()) for x in f.read().split(',')]
    return memory


memory = get_program()
inqs = [Queue() for _ in range(50)]
outqs = [Queue() for _ in range(50)]
computers = []
for i in range(50):
    t = IntCode(memory.copy(), inqs[i], outqs[i], False)
    computers.append(t)
    inqs[i].put(i)

trying_to_read = [0 for _ in range(50)]
nat = None
done = False
last_y_nat = None
while not done:
    for i in range(50):
        op = computers[i].tick()
        if op == 3:
            trying_to_read[i] += 1
        elif op == 4:
            trying_to_read[i] = 0

        if outqs[i].qsize() == 3:
            to = outqs[i].get()
            x = outqs[i].get()
            y = outqs[i].get()
            if to == 255:
                nat = (x, y)
            else:
                inqs[to].put(x)
                inqs[to].put(y)
    if all(q.empty() for q in inqs) and all(x > 150 for x in trying_to_read):
        trying_to_read = [0 for _ in range(50)]
        inqs[0].put(nat[0])
        inqs[0].put(nat[1])
        print('sent', nat[1])
        if nat[1] == last_y_nat:
            print(nat[1])
            done = True
        last_y_nat = nat[1]
