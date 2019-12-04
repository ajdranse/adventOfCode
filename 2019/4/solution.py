part1 = []
part2 = []
for x in range(168630, 718098+1):
    # two adjacent are the same
    # never decrease
    # part 2: not all repeated digits are repeated more than twice
    digits = [int(d) for d in str(x)]
    increasing = True
    doubles = {}
    for i in range(0, 5):
        if digits[i] > digits[i+1]:
            increasing = False
            break
        if digits[i] == digits[i+1]:
            if digits[i] not in doubles:
                doubles[digits[i]] = 2
            else:
                doubles[digits[i]] += 1

    if increasing and len(doubles) > 0:
        part1.append(x)

    if increasing and 2 in doubles.values():
        part2.append(x)

print(len(part1))
print(len(part2))
