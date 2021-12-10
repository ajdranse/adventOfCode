with open('10.in') as f:
    lines = f.read().splitlines()

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
closingpoints = {')': 1, ']': 2, '}': 3, '>': 4}

part1 = 0
part2 = []
for l in lines:
    opened = []
    corrupted = False
    for c in l:
        if c in pairs.keys():
            opened.append(c)
        else:
            # closing
            o = opened.pop()
            if c != pairs[o]:
                part1 += points[c]
                corrupted = True
                break
    if not corrupted:
        # must be incomplete
        closingscore = 0
        while len(opened) > 0:
            o = opened.pop()
            closingscore *= 5
            closingscore += closingpoints[pairs[o]]
        part2.append(closingscore)

print('part1: ', part1)
part2 = sorted(part2)
print('part2: ', part2[len(part2)//2])
