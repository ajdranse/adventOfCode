from bidict import bidict
from collections import defaultdict


inp = []
with open('5.in') as f:
    inp = [x.strip() for x in f.readlines()]

rules = defaultdict(list)
updates = []
for line in inp:
    if '|' in line:
        (first, second) = line.split('|')
        rules[int(first)].append(int(second))
    elif ',' in line:
        updates.append(list(map(int, line.split(','))))

valid = []
fixed = []
for update in updates:
    # arbitrary large number
    prev_num_rules = 1_000_000

    # set up a bidict of page -> number of rules it has that are relevant to this update
    # the first page will have the most rules, the second the second-most, ..., the last will have no rules
    page_to_numrules = bidict({page: len(set(rules[page]).intersection(set(update))) for page in update})

    # for each page
    for page in update:
        # if it has more rules than the previous page, it's out of order
        if page_to_numrules[page] > prev_num_rules:
            # for part 2, fix this update by pulling out the pages in descending order of number of rules
            fixed.append([page_to_numrules.inverse[i] for i in range(len(update)-1, -1, -1)])
            break
        prev_num_rules = page_to_numrules[page]
    else:
        valid.append(update)


s = sum([v[len(v)//2] for v in valid])
print('part1: ', s)

s = sum([f[len(f)//2] for f in fixed])
print('part2: ', s)
