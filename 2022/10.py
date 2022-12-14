# addx V adds V to x register, 2 cycles
# noop, 1 cycle
class Computer:
    def __init__(self, instructions):
        self.X = 1
        self.instructions = instructions
        self.cur_op = None
        self.cur_param = None
        self.cycles_left = 0

    def start_cycle(self):
        if self.cycles_left == 0 and len(self.instructions) > 0:
            instr = self.instructions.pop(0)
            if ' ' in instr:
                self.cur_op, self.cur_param = instr.split()
            else:
                self.cur_op = instr
                self.cur_param = None

            if self.cur_op == 'addx':
                self.cycles_left = 2
                self.cur_param = int(self.cur_param)
            elif self.cur_op == 'noop':
                self.cycles_left = 1
            # print(f'starting op {self.cur_op} with param {self.cur_param}, cycles left {self.cycles_left}')

    def end_cycle(self):
        if self.cur_op is not None:
            self.cycles_left -= 1
            # print(f'{self.cycles_left} cycles left in op {self.cur_op}')
            if self.cycles_left == 0:
                if self.cur_op == 'addx':
                    # print(f'done addx, adding {self.cur_param} to {self.X}, giving {self.X + self.cur_param}')
                    self.X += self.cur_param

                self.cur_op = None
                self.cur_param = None
        return self.instructions

    def get_X(self):
        return self.X


test = [
'noop',
'addx 3',
'addx -5',
]

test2 = [
    'addx 15',
    'addx -11',
    'addx 6',
    'addx -3',
    'addx 5',
    'addx -1',
    'addx -8',
    'addx 13',
    'addx 4',
    'noop',
    'addx -1',
    'addx 5',
    'addx -1',
    'addx 5',
    'addx -1',
    'addx 5',
    'addx -1',
    'addx 5',
    'addx -1',
    'addx -35',
    'addx 1',
    'addx 24',
    'addx -19',
    'addx 1',
    'addx 16',
    'addx -11',
    'noop',
    'noop',
    'addx 21',
    'addx -15',
    'noop',
    'noop',
    'addx -3',
    'addx 9',
    'addx 1',
    'addx -3',
    'addx 8',
    'addx 1',
    'addx 5',
    'noop',
    'noop',
    'noop',
    'noop',
    'noop',
    'addx -36',
    'noop',
    'addx 1',
    'addx 7',
    'noop',
    'noop',
    'noop',
    'addx 2',
    'addx 6',
    'noop',
    'noop',
    'noop',
    'noop',
    'noop',
    'addx 1',
    'noop',
    'noop',
    'addx 7',
    'addx 1',
    'noop',
    'addx -13',
    'addx 13',
    'addx 7',
    'noop',
    'addx 1',
    'addx -33',
    'noop',
    'noop',
    'noop',
    'addx 2',
    'noop',
    'noop',
    'noop',
    'addx 8',
    'noop',
    'addx -1',
    'addx 2',
    'addx 1',
    'noop',
    'addx 17',
    'addx -9',
    'addx 1',
    'addx 1',
    'addx -3',
    'addx 11',
    'noop',
    'noop',
    'addx 1',
    'noop',
    'addx 1',
    'noop',
    'noop',
    'addx -13',
    'addx -19',
    'addx 1',
    'addx 3',
    'addx 26',
    'addx -30',
    'addx 12',
    'addx -1',
    'addx 3',
    'addx 1',
    'noop',
    'noop',
    'noop',
    'addx -9',
    'addx 18',
    'addx 1',
    'addx 2',
    'noop',
    'noop',
    'addx 9',
    'noop',
    'noop',
    'noop',
    'addx -1',
    'addx 2',
    'addx -37',
    'addx 1',
    'addx 3',
    'noop',
    'addx 15',
    'addx -21',
    'addx 22',
    'addx -6',
    'addx 1',
    'noop',
    'addx 2',
    'addx 1',
    'noop',
    'addx -10',
    'noop',
    'noop',
    'addx 20',
    'addx 1',
    'addx 2',
    'addx 2',
    'addx -6',
    'addx -11',
    'noop',
    'noop',
    'noop',
]

lines = []
with open('10.in') as f:
    lines = [x.strip() for x in f.readlines()]

# lines = test2

c = Computer(lines)
to_check = [20, 60, 100, 140, 180, 220]
s = 0
x = 0
line_str = ''
left = lines
while len(left) > 0:
    x += 1
    c.start_cycle()
    if x in to_check:
        s += x * c.get_X()
    crt_pos = (x-1) % 40
    if abs(c.get_X() - crt_pos) < 2:
        line_str += '#'
    else:
        line_str += '.'
    # print(f'sprite at {c.get_X()}, crt printing pixel {crt_pos}, line is {line_str}')
    if x % 40 == 0:
        print(line_str)
        line_str = ''
    left = c.end_cycle()
print('part1', s)
