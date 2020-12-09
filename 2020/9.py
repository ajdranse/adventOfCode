nums = []
preamble_len = 25
with open("9.in") as f:
    for line in f:
        nums.append(int(line))

for idx, num in enumerate(nums):
    if idx < preamble_len:
        continue
    found = any([nums[i] + nums[j] == num for i in range(idx - preamble_len, idx) for j in range(i + 1, idx)])
    if not found:
        print('part1: {}'.format(num))
        combinations = [nums[i:i+j] for i in range(0, idx) for j in range(1, idx - i + 1)]
        for c in combinations:
            if sum(c) == num:
                print('part2: {}'.format(min(c) + max(c)))
                break
        break


