import re

lines = []
with open('2.in') as f:
    lines = [x for x in f.read().splitlines()]

part1 = 0
part2 = 0
for line in lines:
    split = re.search('(\d+)-(\d+) (.): (.+)', line, re.IGNORECASE);
    if split:
        l = int(split.group(1))
        h = int(split.group(2))
        c = split.group(3)
        s = split.group(4)
        count = s.count(c)
        # print(l, h, c, s, count)
        if count >= l and count <= h:
            part1 += 1

        l_has = s[l-1] == c
        h_has = s[h-1] == c
        # xor the checks
        if l_has != h_has:
            part2 += 1
print('part 1')
print(part1)

print('part 2')
print(part2)
