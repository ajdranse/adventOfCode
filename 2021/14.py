import math

from collections import Counter


with open('14.in') as f:
    lines = f.read().splitlines()

polymer = lines[0]

pairs = {}
for l in lines[2:]:
    (start, end) = l.split(' -> ')
    pairs[start] = end

ppairs = Counter()
for i in range(len(polymer) - 1):
    ppairs[polymer[i:i+2]] += 1

step = 0
while step < 40:
    old_ppairs = ppairs.copy()
    for k, v in old_ppairs.items():
        if v > 0:
            ppairs[k] -= v
            ins = pairs[k]
            ppairs[k[0] + ins] += v
            ppairs[ins + k[1]] += v
    step += 1
    if step == 10:
        counts = Counter()
        for k, v in ppairs.items():
            counts[k[0]] += v / 2
            counts[k[1]] += v / 2
        print('part1: ', math.ceil(counts.most_common()[0][1] - counts.most_common()[-1][1]))

counts = Counter()
for k, v in ppairs.items():
    counts[k[0]] += v / 2
    counts[k[1]] += v / 2
print('part2: ', math.ceil(counts.most_common()[0][1] - counts.most_common()[-1][1]))
