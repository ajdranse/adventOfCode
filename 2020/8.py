def run(instructions):
    acc = 0
    ip = 0
    seen = set()

    while ip not in seen:
        if ip == len(instructions):  # terminated
            return (acc, True)
        seen.add(ip)
        (instr, val) = instructions[ip]
        if instr == 'nop':
            ip += 1
        elif instr == 'acc':
            ip += 1
            acc += val
        elif instr == 'jmp':
            ip += val
        else:
            raise('Invalid instruction: {}'.format(instr))

    return (acc, False)


instructions = []
with open("8.in") as f:
# with open("8.test") as f:
    for line in f:
        (op, val) = line.split(' ')
        val = int(val)
        instructions.append((op, val))

(acc, terminated) = run(instructions)
print('part1: {}'.format(acc))

for to_modify in range(len(instructions)):
    modified = instructions.copy()
    instr_op = modified[to_modify][0]
    instr_val = modified[to_modify][1]
    if instr_op == 'acc':
        continue
    elif instr_op == 'nop':
        modified[to_modify] = ('jmp', instr_val)
    elif instr_op == 'jmp':
        modified[to_modify] = ('nop', instr_val)

    (acc, terminated) = run(modified)
    if terminated:
        print('part2: {}'.format(acc))
        break
