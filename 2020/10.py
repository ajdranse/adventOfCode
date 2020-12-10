from anytree import Node, PreOrderIter

jolts = []
# with open("10.test") as f:
# with open("10.test2") as f:
with open("10.in") as f:
    for line in f:
        jolts.append(int(line))

jolts.append(0)
jolts = sorted(jolts)
jolts.append(jolts[-1] + 3)

diffs = [jolts[i+1] - jolts[i] for i in range(len(jolts) - 1)]
agg = {}
for d in diffs:
    if d not in agg:
        agg[d] = 1
    else:
        agg[d] += 1

print('part1: {}'.format(agg[1] * agg[3]))

seen = {}
def find_solutions(idx):
    # memoisation
    if idx in seen:
        return seen[idx]

    # base case
    if idx == len(jolts) - 1: # i.e. testing the last position
        return 1  # only way is to go to the last jolt

    ways = 0
    for i in range(idx + 1, idx + 4):  # for the rest of the possibly valid indices
        # if it's actually valid
        if i < len(jolts) and jolts[i] - jolts[idx] <= 3:
            # the number of ways to solve is the sum of all the valid ways to solve from this index
            ways += find_solutions(i)

    # store in seen
    seen[idx] = ways
    return ways

print('part2: {}'.format(find_solutions(0)))
