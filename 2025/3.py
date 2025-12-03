def calc(banks, num_bats):
    ret = 0
    for b in banks:
        j = 0
        start = 0
        for i in range(num_bats):
            sl = b[start : len(b) - (num_bats - i - 1)]
            idx = sl.index(max(sl)) + start

            j *= 10
            j += b[idx]

            start = idx + 1
        ret += j
    return ret


banks = []
with open('3.in') as f:
    banks = [[int(y) for y in x.strip()] for x in f.readlines()]

p1 = calc(banks, 2)
p2 = calc(banks, 12)
print(f'{p1=}, {p2=}')
