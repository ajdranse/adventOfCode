from collections import Counter

nums = []
with open('input') as f:
    nums = [int(x) for x in f.read().strip()]

layers = []
counters = []
layer = []
for i, n in enumerate(nums):
    layer.append(n)
    if len(layer) == 25 * 6:
        layers.append(layer)
        counters.append(Counter(sorted(layer)))
        layer = []

min_layer = None
for i, l in enumerate(counters):
    if min_layer is None or l[0] < min_layer[0]:
        min_layer = l
print('part 1: {}'.format(min_layer[1] * min_layer[2]))

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
