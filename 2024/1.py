from collections import defaultdict

left = []
right = []
r_map = defaultdict(int)
with open('1.in') as f:
    for x in f.readlines():
        (l, r) = map(int, x.strip().split())
        left.append(l)
        right.append(r)
        r_map[r] += 1

left.sort()
right.sort()

diff = 0
sim = 0
for (l, r) in zip(left, right):
    diff += abs(l - r)
    sim += (l * r_map[l])

print('part1: ', diff)
print('part2: ', sim)
