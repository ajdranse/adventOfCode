def run(code):
    idx = 0
    while True:
        opcode = code[idx]
        if opcode == 1:
            operand1 = code[code[idx+1]]
            operand2 = code[code[idx+2]]
            code[code[idx+3]] = operand1 + operand2
        elif opcode == 2:
            operand1 = code[code[idx+1]]
            operand2 = code[code[idx+2]]
            code[code[idx+3]] = operand1 * operand2
        elif opcode == 99:
            return code
        else:
            print(f'Error, unknown opcode: {opcode}')
            raise
        idx += 4


# test = [[1, 0, 0, 0, 99],  [2, 3, 0, 3, 99],  [2, 4, 4, 5, 99, 0],  [1, 1, 1, 4, 99, 5, 6, 0, 99]]
# for case in test:
#     print(f'{case} gives:')
#     run(case)
#     print(f'{case}')
code = None
with open('input') as f:
    code = [int(x.strip()) for x in f.read().split(',')]
print(f'input: {code}')
part1 = code.copy()
part1[1] = 12
part1[2] = 2
run(part1)
print(f'output: {part1}')

for noun in range(0, 99):
    for verb in range(0, 99):
        test = code.copy()
        test[1] = noun
        test[2] = verb
        run(test)
        if test[0] == 19690720:
            print(f'match: noun {noun} verb {verb} {100 * noun + verb}')
