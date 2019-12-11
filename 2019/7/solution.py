import itertools
from queue import Queue
from intcode import IntCode


def part1(memory):
    max_signal = 0
    max_order = []
    for order in itertools.permutations([0, 1, 2, 3, 4], 5):
        signal = 0
        input_queue = Queue()
        output_queue = Queue()
        for i in order:
            input_queue.put(i)
            input_queue.put(signal)
            cur_thread = IntCode(memory.copy(), input_queue, output_queue)
            cur_thread.start()
            cur_thread.join()
            signal = output_queue.get()

        if signal > max_signal:
            max_signal = signal
            max_order = order
    print(max_order, max_signal)


def part2(memory):
    max_signal = 0
    max_order = []
    for order in itertools.permutations([5, 6, 7, 8, 9], 5):
        signal = 0
        queues = [Queue() for _ in range(5)]
        threads = []
        for idx, phase in enumerate(order):
            queues[idx].put(phase)
            cur_thread = IntCode(memory.copy(), queues[idx], queues[(idx + 1) % 5])
            threads.append(cur_thread)
            cur_thread.start()

        queues[0].put(0)
        for t in threads:
            t.join()

        signal = queues[0].get()

        if signal > max_signal:
            max_signal = signal
            max_order = order
    print(max_order, max_signal)


with open('input') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    print('part 1')
    part1(memory.copy())

    print('part 2')
    part2(memory.copy())
