p1 = 0
p2 = 0
dial = 50
with open('1.in') as f:
    for x in f.readlines():
        x = x.strip()
        mult = -1 if x[0] == 'L' else 1
        val = int(x[1:])
        if val >= 100:
            # full rotations
            p2 += (val // 100)
            val = val % 100

        new_dial = dial + (mult * val)
        if new_dial == 100:
            new_dial = 0

        while new_dial > 100:
            new_dial = new_dial - 100
            if dial != 0:
                p2 += 1
        while new_dial < 0:
            new_dial = new_dial + 100
            if dial != 0:
                p2 += 1

        if new_dial == 0:
            p1 += 1
            p2 += 1

        dial = new_dial
print(f'{p1=}, {p2=}')
