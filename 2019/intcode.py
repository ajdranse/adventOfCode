from threading import Thread


def print_grid(grid, val_map):
    '''prints a grid, where the grid is a dict of (x, y) to int values.
        uses provided map to determine what to print.
    '''
    outs = ''
    for y in range(max(grid, key=lambda g: g[1])[1] + 1):
        for x in range(max(grid, key=lambda g: g[0])[0] + 1):
            if (x, y) in grid:
                outs += val_map[grid[(x, y)]]
            else:
                outs += val_map[0]
        outs += '\n'
    print(outs)


class IntCode(Thread):
    def __init__(self, memory, input_queue, output_queue):
        super(IntCode, self).__init__()
        self.memory = memory
        self.opcode = 0
        self.modes = []
        self.ip = 0
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.relative_base = 0

    def get(self, idx):
        if idx < 0:
            raise Exception('Accessing negative index in memory: {}'.format(idx))
        if idx >= len(self.memory):
            self.memory += [0] * (idx - len(self.memory) + 1)
        return self.memory[idx]

    def set(self, idx, val):
        if idx < 0:
            raise Exception('Accessing negative index in memory: {}'.format(idx))
        if idx >= len(self.memory):
            self.memory += [0] * (idx - len(self.memory) + 1)

        self.memory[idx] = val

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

    def get_addresses(self, count):
        ret = ()
        for i in range(count):
            if self.modes[i] == 1:
                ret += (self.ip+i+1, )
            elif self.modes[i] == 2:
                ret += (self.get(self.ip+i+1) + self.relative_base, )
            elif self.modes[i] == 0:
                ret += (self.get(self.ip+i+1), )
            else:
                raise Exception('Unknown mode {}'.format(self.modes[i]))
        return ret

    def add(self):
        (first, second, third) = self.get_addresses(3)
        self.set(third, self.get(first) + self.get(second))
        self.ip += 4

    def mult(self):
        (first, second, third) = self.get_addresses(3)
        self.set(third, self.get(first) * self.get(second))
        self.ip += 4

    def input(self):
        first = self.get_addresses(1)[0]
        val = self.input_queue.get()
        self.set(first, val)
        self.ip += 2

    def output(self):
        first = self.get_addresses(1)[0]
        self.output_queue.put(self.get(first))
        self.ip += 2

    def jump_if_true(self):
        (first, second) = self.get_addresses(2)
        if self.get(first) != 0:
            self.ip = self.get(second)
        else:
            self.ip += 3

    def jump_if_false(self):
        (first, second) = self.get_addresses(2)
        if self.get(first) == 0:
            self.ip = self.get(second)
        else:
            self.ip += 3

    def lt(self):
        (first, second, third) = self.get_addresses(3)
        self.set(third, 1 if self.get(first) < self.get(second) else 0)
        self.ip += 4

    def eq(self):
        (first, second, third) = self.get_addresses(3)
        self.set(third, 1 if self.get(first) == self.get(second) else 0)
        self.ip += 4

    def update_relative_base(self):
        first = self.get_addresses(1)[0]
        self.relative_base += self.get(first)
        self.ip += 2

    def run(self):
        self.opcode = self.get(self.ip)
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
            elif self.opcode == 9:  # update relative base
                self.update_relative_base()
            else:
                print('Error, unknown opcode: {}'.format(self.opcode))
                break
            self.opcode = self.get(self.ip)
