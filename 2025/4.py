import copy
import png


def count(data):
    ret = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != 1:
                continue

            adj = 0
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nx = x+dx
                ny = y+dy
                if nx < 0 or ny < 0 or nx >= len(data[y]) or ny >= len(data):
                    continue
                adj += data[ny][nx]
                if adj == 4:
                    break
            else:
                ret += 1
    return ret


def remove(inp):
    ret = copy.deepcopy(inp)
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] != 1:
                continue

            adj = 0
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nx = x+dx
                ny = y+dy
                if nx < 0 or ny < 0 or nx >= len(inp[y]) or ny >= len(inp):
                    continue
                adj += inp[ny][nx]
            if adj < 4:
                ret[y][x] = 0
    return ret


def s(data):
    ret = 0
    for r in data:
        ret += sum(r)
    return ret


def gen_img(s, i):
    f = open(f'png{i:04d}.png', 'wb')
    w = png.Writer(len(s[0]), len(s), greyscale=True, bitdepth=1)
    w.write(f, s)
    f.close()


with open('4.in') as f:
    lines = [x.strip() for x in f.readlines()]
data = []
for l in lines:
    data.append([1 if x == '@' else 0 for x in l])

p1 = count(data)
print(f'{p1=}')

p2 = p1
i = 0
while True:
    gen_img(data, i)
    i += 1
    new_data = remove(data)
    if s(new_data) == s(data):
        break

    new_access = count(new_data)
    p2 += new_access
    data = new_data

print(p2)
