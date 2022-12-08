lines = []
with open('8.in') as f:
    lines = [x.strip() for x in f.readlines()]

trees = []
# for line in test:
for line in lines:
    row = []
    for c in line:
        t = int(c)
        row.append(t)
    trees.append(row)

visible = 0
for y in range(len(trees)):
    if y == 0 or y == len(trees) - 1:
        visible += len(trees[y])
        continue

    for x in range(len(trees[y])):
        if x == 0 or x == len(trees[y]) - 1:
            # all trees on left/right edges are visible
            visible += 1
            continue

        t = trees[y][x]
        visibleUp = True
        visibleDown = True
        visibleLeft = True
        visibleRight = True

        for y2 in range(y-1, -1, -1):
            if trees[y2][x] >= t:
                visibleUp = False
                break

        for y2 in range(y+1, len(trees)):
            if trees[y2][x] >= t:
                visibleDown = False
                break

        for x2 in range(x-1, -1, -1):
            if trees[y][x2] >= t:
                visibleLeft = False
                break

        for x2 in range(x+1, len(trees[y])):
            if trees[y][x2] >= t:
                visibleRight = False
                break

        if visibleUp or visibleDown or visibleLeft or visibleRight:
            visible += 1
print('part1', visible)

best_score = 0
for y in range(len(trees)):
    for x in range(len(trees[y])):
        t = trees[y][x]
        score = 1

        can_see = 0
        for y2 in range(y-1, -1, -1):
            can_see += 1
            if trees[y2][x] >= t:
                break
        score *= can_see

        can_see = 0
        for y2 in range(y+1, len(trees)):
            can_see += 1
            if trees[y2][x] >= t:
                break
        score *= can_see

        can_see = 0
        for x2 in range(x-1, -1, -1):
            can_see += 1
            if trees[y][x2] >= t:
                break
        score *= can_see

        can_see = 0
        for x2 in range(x+1, len(trees[y])):
            can_see += 1
            if trees[y][x2] >= t:
                break
        score *= can_see

        if score > best_score:
            best_score = score

print('part2', best_score)
