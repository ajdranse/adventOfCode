from queue import Queue
from intcode import IntCode

tests = [
    [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99],
    [1102, 34915192, 34915192, 7, 4, 7, 99, 0],
    [104, 1125899906842624, 99]
]

for test in tests:
    q = Queue()
    t = IntCode(test.copy(), None, q)
    t.start()
    t.join()

    output = []
    while not q.empty():
        output.append(str(q.get()))
    print(','.join(output))

with open('input') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    print('part 1')
    inq = Queue()
    outq = Queue()
    t = IntCode(memory.copy(), inq, outq)
    t.start()
    inq.put(1)
    t.join()
    output = []
    while not outq.empty():
        output.append(str(outq.get()))
    print(','.join(output))

    print('part 2')
    t = IntCode(memory.copy(), inq, outq)
    t.start()
    inq.put(2)
    t.join()
    output = []
    while not outq.empty():
        output.append(str(outq.get()))
    print(','.join(output))
