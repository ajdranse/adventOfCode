lines = []
with open('2.in') as f:
    lines = f.read().splitlines()

pos = 0
depth1 = 0
depth2 = 0
aim = 0

for l in lines:
    val = int(l.split(' ')[1])
    if 'forward' in l:
        pos += val
        depth2 += (aim * val)
    elif 'down' in l:
        depth1 += val
        aim += val
    elif 'up' in l:
        depth1 -= val
        aim -= val

print('part 1')
print(pos, depth1, pos*depth1)

print('part 2')
print(pos, depth2, pos*depth2)

