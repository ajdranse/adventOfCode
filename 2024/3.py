import re

inp = []
with open ('3.in') as f:
    inp = ''.join([x.strip() for x in f.readlines()])

# mul(X, Y) = X*Y; x,y 1-3 digits
# do() enables mul
# don't() disabled mul

r = r'mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don\'t)\(\)'
matches = re.findall(r, inp)
s1 = 0
s2 = 0
enabled = True
for m in matches:
    if m[2] == 'do':
        enabled = True
    elif m[3] == 'don\'t':
        enabled = False
    if m[0] != '' and m[1] != '':
        cur = int(m[0]) * int(m[1])
        s1 += cur
        if enabled:
            s2 += cur
print('part1', s1)
print('part2', s2)
