import re

def parse():
    with open('17.in') as f:
        inp = [x.strip() for x in f.readlines()]

    program = A = B = C = None
    for l in inp:
        m = re.match(r'Register [ABC]: (\d+)', l)
        if m:
            g = m.groups()
            if A == None:
                A = int(g[0])
            elif B == None:
                B = int(g[0])
            else:
                C = int(g[0])
        m = re.match(r'Program: (.*)$', l)
        if m:
            program = list(map(int, m.groups()[0].split(',')))
    return (A, B, C, program)

def combo(o, A, B, C):
    if o <= 3:
        return o
    if o == 4:
        return A
    if o == 5:
        return B
    if o == 6:
        return C
    raise ValueError(o)

def run(A, B, C, program, quine=False):
    ip = 0

    output = []
    while ip < len(program)-1:
        opcode = program[ip]
        operand = program[ip+1]
        if opcode == 0:
            # 0: adv - A / 2^combo_operand -> A reg
            A = A // pow(2, combo(operand, A, B, C))
        elif opcode == 1:
            # 1: bxl - B XOR literal_operand -> B reg
            B = B ^ operand
        elif opcode == 2:
            # 2: bst - combo_operand % 8 -> B reg
            B = combo(operand, A, B, C) % 8
        elif opcode == 3:
            # 3: jnz - nothing if A == 0, else jumps to literal_operand, ip not increased by 2
            if A != 0:
                ip = operand
                continue
        elif opcode == 4:
            # 4: bxc - B XOR C -> B
            B = B ^ C
        elif opcode == 5:
            # 5: out - combo_operand % 8 -> outputs
            output.append(combo(operand, A, B, C) % 8)
            if quine and program[:len(output)] != output:
                print(f'already failed with {output=}')
                return (output, A, B, C)
        elif opcode == 6:
            # 6: bdv - A / 2^combo_operand -> B reg
            B = A // pow(2, combo(program[ip+1], A, B, C))
        elif opcode == 7:
            # 7: cdv - A / 2^combo_operand -> C reg
            C = A // pow(2, combo(program[ip+1], A, B, C))
        else:
            raise ValueError(opcode)

        ip += 2
    return (output, A, B, C)

if __name__ == '__main__':
    A, B, C, program = parse()
    output, A, B, C = run(A, B, C, program)
    print('part1:', ','.join([str(x) for x in output]))

    # program input is: 2,4,1,1,7,5,4,7,1,4,0,3,5,5,3,0
    # decodes to:
    # print: ((((A%8)^1)^(A // pow(2, ((A%8)^1))) ^ 4) % 8)
    # A = A >> 3
    # repeat until A == 0
    prog = lambda a: ((((a%8)^1)^(a // pow(2, ((a%8)^1))) ^ 4) % 8)

    # now build up starting values of A from ending condition of 0
    prev = [0]
    program.reverse()
    for idx in range(len(program)):
        prev = [a for p in prev for a in range(p<<3, (p+1)<<3) if prog(a) == program[idx]]
    print('part2:', min(prev))
