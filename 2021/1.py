
lines = []
with open('1.in') as f:
    lines = [int(x) for x in f.read().splitlines()]
# lines = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

print('part 1')
print(sum([1 if lines[i+1] - lines[i] > 0 else 0 for i in range(len(lines) - 1)]))

print('part 2')
print(sum([1 if sum(lines[i+1:i+4]) - sum(lines[i:i+3]) > 0 else 0 for i in range(len(lines) - 3)]))
