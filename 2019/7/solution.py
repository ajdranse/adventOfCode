import itertools
from queue import Queue
from threading import Thread


def run(memory, i, input_queue, output_queue):
    ip = 0
    while True:
        opcode = memory[ip]
        modes = []
        if opcode > 100:
            raw_modes = int(opcode / 100)
            opcode = opcode % 100
            while raw_modes > 0:
                modes.append(raw_modes % 10)
                raw_modes = int(raw_modes / 10)
        while len(modes) < 4:
            modes.append(0)

        if opcode == 1:  # add
            first = memory[ip+1] if modes[0] else memory[memory[ip+1]]
            second = memory[ip+2] if modes[1] else memory[memory[ip+2]]
            memory[memory[ip+3]] = first + second
            ip += 4
        elif opcode == 2:  # mult
            first = memory[ip+1] if modes[0] else memory[memory[ip+1]]
            second = memory[ip+2] if modes[1] else memory[memory[ip+2]]
            memory[memory[ip+3]] = first * second
            ip += 4
        elif opcode == 3:  # input
            memory[memory[ip+1]] = input_queue.get(True)
            ip += 2
        elif opcode == 4:  # output
            first = ip+1 if modes[0] else memory[ip+1]
            output_queue.put(memory[first])
            ip += 2
        elif opcode == 5:  # jump-if-true
            first = memory[ip+1] if modes[0] else memory[memory[ip+1]]
            second = memory[ip+2] if modes[1] else memory[memory[ip+2]]
            if first != 0:
                ip = second
            else:
                ip += 3
        elif opcode == 6:  # jump-if-false
            first = memory[ip+1] if modes[0] else memory[memory[ip+1]]
            second = memory[ip+2] if modes[1] else memory[memory[ip+2]]
            if first == 0:
                ip = second
            else:
                ip += 3
        elif opcode == 7:  # less-than
            first = memory[ip+1] if modes[0] else memory[memory[ip+1]]
            second = memory[ip+2] if modes[1] else memory[memory[ip+2]]
            memory[memory[ip+3]] = 1 if first < second else 0
            ip += 4
        elif opcode == 8:  # equals
            first = memory[ip+1] if modes[0] else memory[memory[ip+1]]
            second = memory[ip+2] if modes[1] else memory[memory[ip+2]]
            memory[memory[ip+3]] = 1 if first == second else 0
            ip += 4
        elif opcode == 99:  # exit
            return
        else:
            print('Error, unknown opcode: {}'.format(opcode))
            raise


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
            cur_thread = Thread(target=run, args=(memory.copy(), i, input_queue, output_queue))
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
            cur_thread = Thread(target=run, args=(memory.copy(), idx, queues[idx], queues[(idx + 1) % 5]))
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
