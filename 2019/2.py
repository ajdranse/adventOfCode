def run(memory):
    idx = 0
    while True:
        opcode = memory[idx]
        if opcode == 1:  # add
            memory[memory[idx+3]] = memory[memory[idx+1]] + memory[memory[idx+2]]
            idx += 4
        elif opcode == 2:  # mult
            memory[memory[idx+3]] = memory[memory[idx+1]] * memory[memory[idx+2]]
            idx += 4
        elif opcode == 99:  # exit
            return memory
        else:
            print(f'Error, unknown opcode: {opcode}')
            raise


def run2(code):
    for noun in range(0, 99):
        for verb in range(0, 99):
            test = code.copy()
            test[1] = noun
            test[2] = verb
            run(test)
            if test[0] == 19690720:
                print(f'match: noun {noun} verb {verb} = {100 * noun + verb}')
                return


# test = [[1, 0, 0, 0, 99],  [2, 3, 0, 3, 99],  [2, 4, 4, 5, 99, 0],  [1, 1, 1, 4, 99, 5, 6, 0, 99]]
# for case in test:
#     print(f'{case} gives:')
#     run(case)
#     print(f'{case}')
memory = None
with open('2.in') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
part1 = memory.copy()
part1[1] = 12
part1[2] = 2
run(part1)
print(f'{part1}')

run2(memory)
