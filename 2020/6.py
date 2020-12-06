from collections import defaultdict

answers = []
# with open("6.test") as f:
with open("6.in") as f:
    answer = defaultdict(int)
    for line in f:
        if line == "\n" and len(answer) > 0:
            answers.append(answer)
            answer = defaultdict(int)
        else:
            answer['total'] += 1
            for a in line.rstrip():
                answer[a] += 1
    answers.append(answer)

any_yes = 0
all_yes = 0
for a in answers:
    any_yes += (len(a.keys()) - 1)
    all_num = a['total']
    for k in a:
        if k != 'total' and a[k] == all_num:
            all_yes += 1
print('part1: {}'.format(any_yes))
print('part2: {}'.format(all_yes))
