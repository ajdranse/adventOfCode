def calc_safety(r):
    diffs = [b - a for a, b in zip(r, r[1:])]
    all_lt_zero = all([d < 0 for d in diffs])
    all_gt_zero = all([d > 0 for d in diffs])
    all_gradual = all([abs(d) <= 3 and abs(d) >= 1 for d in diffs])
    if (all_lt_zero or all_gt_zero) and all_gradual:
        return True
    return False


num_safe_1 = 0
num_safe_2 = 0
with open('2.in') as f:
    for x in f.readlines():
        report = list(map(int, x.strip().split()))
        if calc_safety(report):
            num_safe_1 += 1
            num_safe_2 += 1
        else:
            for x in range(len(report)):
                if calc_safety([r for idx, r in enumerate(report) if idx != x]):
                    num_safe_2 += 1
                    break

print('part1:', num_safe_1)
print('part2:', num_safe_2)
