import itertools


def run(memory, input_val):
    outputs = []
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
            memory[memory[ip+1]] = input_val
            inputs_taken += 1
            ip += 2
        elif opcode == 4:  # output
            first = ip+1 if modes[0] else memory[ip+1]
            outputs.append(memory[first])
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
            return outputs
        else:
            print('Error, unknown opcode: {}'.format(opcode))
            raise


# test = [
#     [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
# ]
# for case in test:
#     signal = 0
#     for i in [4, 3, 2, 1, 0]:
#         print('calling with inputs {} and {}'.format(i, signal))
#         signal = run(case.copy(), [i, signal])[0]
#     print(signal)

with open('input') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    print('part 1')
    max_signal = 0
    max_order = []
    for order in itertools.permutations([0, 1, 2, 3, 4], 5):
        signal = 0
        for i in order:
            signal = run(memory.copy(), [i, signal])[0]
        if signal > max_signal:
            max_signal = signal
            max_order = order
    print(max_order, max_signal)

#     print('part 2')
#     max_signal = 0
#     max_order = []
#     for order in itertools.permutations([5, 6, 7, 8, 9], 5):
#         signal = 0
#         for i in order:
#             signal = run(memory.copy(), [i, signal])[0]
#         if signal > max_signal:
#             max_signal = signal
#             max_order = order
#     print(max_order, max_signal)
