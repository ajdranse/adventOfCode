from PIL import Image

instructions = []
with open('6.in') as f:
    lines = f.read().splitlines()
    for line in lines:
        i = line.split(' ')
        if len(i) == 5:  # turn on/off x,y through x',y'
            instructions.append((i[1], i[2].split(','), i[4].split(',')))
        elif len(i) == 4:  # toggle x,y through x',y'
            instructions.append((i[0], i[1].split(','), i[3].split(',')))

img = Image.new('RGB', (1000, 1000), "black")
lights = [0 for _ in range(1000000)]
for i, instr in enumerate(instructions):
    pixels = img.load()
    for x in range(int(instr[1][0]), int(instr[2][0])+1):
        for y in range(int(instr[1][1]), int(instr[2][1])+1):
            idx = y * 1000 + x
            if instr[0] == 'on':
                lights[idx] = 1
                pixels[x, y] = (255, 255, 255)
            elif instr[0] == 'off':
                lights[idx] = 0
                pixels[x, y] = (0, 0, 0)
            elif instr[0] == 'toggle':
                pixels[x, y] = (0, 0, 0) if lights[idx] else (255, 255, 255)
                lights[idx] = 0 if lights[idx] else 1

    img.save('6_{:03d}.png'.format(i), "png")
