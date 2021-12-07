def calc(crabs, part2):
    min_pos = min(crabs)
    max_pos = max(crabs)

    min_fuel = 100000000000000000000000000000
    for i in range(min_pos, max_pos+1):
        if part2:
            # n'th triangular number is n * (n + 1) / 2
            fuel = sum((abs(x - i) * (abs(x - i) + 1) // 2) for x in crabs)
        else:
            fuel = sum(abs(x - i) for x in crabs)

        if fuel < min_fuel:
            min_fuel = fuel

    return min_fuel


lines = [16,1,2,0,4,2,7,1,2,14]

with open('7.in') as f:
    lines = [int(x) for x in f.read().split(',')]

print(f'part 1: {calc(lines, False)}')
print(f'part 2: {calc(lines, True)}')
