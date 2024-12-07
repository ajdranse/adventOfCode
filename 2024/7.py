import itertools

def apply(inputs, combo):
    total = inputs[0]
    for idx, o in enumerate(combo):
        if o == '*':
            total *= inputs[idx+1]
        elif o == '+':
            total += inputs[idx+1]
        elif o == '||':
            total = int(str(total) + str(inputs[idx+1]))
    return total

inp = []
with open('7.in') as f:
    inp = [x.strip() for x in f.readlines()]

part1 = 0
part2 = 0
for l in inp:
    (testval, rest) = l.split(': ')
    testval = int(testval)
    inputs = list(map(int, rest.split(' ')))

    combinations = list(itertools.product(*([['*', '+', '||']] * (len(inputs) - 1))))
    p1c = [x for x in combinations if '||' not in x]
    p2c = [x for x in combinations if '||' in x]

    for combo in p1c:
        total = apply(inputs, combo)
        if total == testval:
            part2 += testval
            part1 += testval
            break
    else:
        for combo in p2c:
            total = apply(inputs, combo)
            if total == testval:
                part2 += testval
                break

print(f'{part1=}')
print(f'{part2=}')
