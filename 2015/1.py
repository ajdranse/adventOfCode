with open('1.in') as f:
    inp = f.read().splitlines()[0]

floor = 0
basement = False
for i, d in enumerate(inp):
    if d == '(':
        floor += 1
    elif d == ')':
        floor -= 1
        if floor < 0 and not basement:
            basement = True
            print('basement on step {}'.format(i+1))

print('ends on {}'.format(floor))
