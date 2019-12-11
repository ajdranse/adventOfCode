from collections import Counter

nums = []
with open('8.in') as f:
    nums = [int(x) for x in f.read().strip()]

layers = []
min_zeroes_layer = None
layer = []
for n in nums:
    layer.append(n)
    if len(layer) == 25 * 6:
        layers.append(layer)
        if min_zeroes_layer is None or Counter(layer)[0] < min_zeroes_layer[0]:
            min_zeroes_layer = Counter(layer)
        layer = []

print('part 1: {}'.format(min_zeroes_layer[1] * min_zeroes_layer[2]))

final = []
for i in range(150):
    for l in layers:
        if l[i] != 2:
            final.append(l[i])
            break

print('part 2:')
output = []
for y in range(6):
    cur = []
    for x in range(25):
        cur.append('.' if final[y*25 + x] else ' ')
    output.append(cur)
for o in output:
    print(''.join(o))
