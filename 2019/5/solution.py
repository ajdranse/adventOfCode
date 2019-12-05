def run(memory, input_val):
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
            ip += 2
        elif opcode == 4:  # output
            first = ip+1 if modes[0] else memory[ip+1]
            print('Output from memory location {}: {}'.format(first, memory[first]))
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
            return memory
        else:
            print(f'Error, unknown opcode: {opcode}')
            raise


# test = [
#     # [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8],
#     # [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8],
#     # [3, 3, 1108, -1, 8, 3, 4, 3, 99],
#     # [3, 3, 1107, -1, 8, 3, 4, 3, 99],
#     # [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9],
#     # [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1],
#     [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,  1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,  999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]  # noqa
# ]
# for case in test:
#     print(f'{case} gives:')
#     run(case.copy(), 7)
#     run(case.copy(), 8)
#     run(case.copy(), 9)

with open('input') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    print('part 1')
    run(memory.copy(), 1)
    print('part 2')
    run(memory.copy(), 5)
