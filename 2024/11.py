from collections import defaultdict


def do(stones, blinks):
    for x in range(blinks):
        new_stones = defaultdict(int)

        for s, c in stones.items():
            if s == 0:
                new_stones[1] += c
            elif len(str(s)) % 2 == 0:
                left_half = int(str(s)[:len(str(s)) // 2])
                right_half = int(str(s)[len(str(s)) // 2 :])
                new_stones[left_half] += c
                new_stones[right_half] += c
            else:
                new_stones[s * 2024] += c
        stones = new_stones
    return sum(stones.values())

with open('11.in') as f:
    inp = [x.strip() for x in f.readlines()][0]
    stones = {int(c): 1 for c in inp.split(' ')}

print('part1:', do(stones, 25))
print('part2:', do(stones, 75))
