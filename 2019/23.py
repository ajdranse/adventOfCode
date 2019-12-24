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
    t.start()
    computers.append(t)

done = False
while not done:
    for q in outqs:
        if not q.empty():
            to = q.get()
            x = q.get()
            y = q.get()
            print(to, x, y)
            if to == 255:
                print(x, y)
                done = True
                break
            inqs[to].put(x)
            inqs[to].put(y)

for i in range(50):
    computers[i].join()
