import itertools
from queue import Queue
from threading import Thread


class IntCode(Thread):
    def __init__(self, memory, input_queue, output_queue):
        super(IntCode, self).__init__()
        self.memory = memory
        self.opcode = 0
        self.modes = []
        self.ip = 0
        self.input_queue = input_queue
        self.output_queue = output_queue

    def parse_opcode(self):
        self.modes = []
        if self.opcode > 100:
            raw_modes = int(self.opcode / 100)
            self.opcode = self.opcode % 100
            while raw_modes > 0:
                self.modes.append(raw_modes % 10)
                raw_modes = int(raw_modes / 10)
        while len(self.modes) < 4:
            self.modes.append(0)

    def add(self):
        first = self.memory[self.ip+1] if self.modes[0] else self.memory[self.memory[self.ip+1]]
        second = self.memory[self.ip+2] if self.modes[1] else self.memory[self.memory[self.ip+2]]
        self.memory[self.memory[self.ip+3]] = first + second
        self.ip += 4

    def mult(self):
        first = self.memory[self.ip+1] if self.modes[0] else self.memory[self.memory[self.ip+1]]
        second = self.memory[self.ip+2] if self.modes[1] else self.memory[self.memory[self.ip+2]]
        self.memory[self.memory[self.ip+3]] = first * second
        self.ip += 4

    def input(self):
        self.memory[self.memory[self.ip+1]] = self.input_queue.get()
        self.ip += 2

    def output(self):
        first = self.ip+1 if self.modes[0] else self.memory[self.ip+1]
        self.output_queue.put(self.memory[first])
        self.ip += 2

    def jump_if_true(self):
        first = self.memory[self.ip+1] if self.modes[0] else self.memory[self.memory[self.ip+1]]
        second = self.memory[self.ip+2] if self.modes[1] else self.memory[self.memory[self.ip+2]]
        if first != 0:
            self.ip = second
        else:
            self.ip += 3

    def jump_if_false(self):
        first = self.memory[self.ip+1] if self.modes[0] else self.memory[self.memory[self.ip+1]]
        second = self.memory[self.ip+2] if self.modes[1] else self.memory[self.memory[self.ip+2]]
        if first == 0:
            self.ip = second
        else:
            self.ip += 3

    def lt(self):
        first = self.memory[self.ip+1] if self.modes[0] else self.memory[self.memory[self.ip+1]]
        second = self.memory[self.ip+2] if self.modes[1] else self.memory[self.memory[self.ip+2]]
        self.memory[self.memory[self.ip+3]] = 1 if first < second else 0
        self.ip += 4

    def eq(self):
        first = self.memory[self.ip+1] if self.modes[0] else self.memory[self.memory[self.ip+1]]
        second = self.memory[self.ip+2] if self.modes[1] else self.memory[self.memory[self.ip+2]]
        self.memory[self.memory[self.ip+3]] = 1 if first == second else 0
        self.ip += 4

    def run(self):
        self.opcode = self.memory[self.ip]
        while self.opcode != 99:
            self.parse_opcode()
            if self.opcode == 1:  # add
                self.add()
            elif self.opcode == 2:  # mult
                self.mult()
            elif self.opcode == 3:  # input
                self.input()
            elif self.opcode == 4:  # output
                self.output()
            elif self.opcode == 5:  # jump-if-true
                self.jump_if_true()
            elif self.opcode == 6:  # jump-if-false
                self.jump_if_false()
            elif self.opcode == 7:  # less-than
                self.lt()
            elif self.opcode == 8:  # equals
                self.eq()
            else:
                print('Error, unknown opcode: {}'.format(self.opcode))
                break
            self.opcode = self.memory[self.ip]


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
