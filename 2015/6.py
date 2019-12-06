instructions = []
with open('6.in') as f:
    lines = f.read().splitlines()
    for line in lines:
        i = line.split(' ')
        if len(i) == 5:  # turn on/off x,y through x',y'
            instructions.append((i[1], i[2].split(','), i[4].split(',')))
        elif len(i) == 4:  # toggle x,y through x',y'
            instructions.append((i[0], i[1].split(','), i[3].split(',')))

lights = [0 for _ in range(1000000)]
for i in instructions:
    for x in range(int(i[1][0]), int(i[2][0])+1):
        for y in range(int(i[1][1]), int(i[2][1])+1):
            idx = y * 1000 + x
            if i[0] == 'on':
                lights[idx] += 1
            elif i[0] == 'off':
                lights[idx] -= 1
                if lights[idx] < 0:
                    lights[idx] = 0
            elif i[0] == 'toggle':
                lights[idx] += 2

on = sum(lights)
print(on)
