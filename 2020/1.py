import itertools

lines = []
with open('1.in') as f:
    lines = [int(x) for x in f.read().splitlines()]

print('part 1')
part1 = [i*j for i, j in itertools.permutations(lines, 2) if i+j == 2020]
for i, j in itertools.permutations(lines, 2):
    if i + j == 2020:
        print(i, j, i*j)
        break

print('part 2')
for i, j, k in itertools.permutations(lines, 3):
    if i + j + k == 2020:
        print(i, j, k, i*j*k)
        break
