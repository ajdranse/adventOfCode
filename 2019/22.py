import re
# 10007 from 0 to 10006
# deal into new stack:
#   reverse order
# cut N cards:
#   move N cards to other end
#   cut 3: indexes 0, 1, 2 become N-3, N-2, N-1
#   cut -4: indexes N-4, N-3, N-2, N-1 become 0, 1, 2, 3
# To deal with increment N
#   N=3: deal into space (m*3) % n until all cards dealt (if len 10: 0, 3, 6, 9, 2, 5, 8, 1, 4, 7)


def run(filename, deck):
    print(filename, len(deck))
    lines = []
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
    for l in lines:
        if l == 'deal into new stack':
            deck = list(reversed(deck))
        else:
            m = re.match(r'deal with increment (\d+)', l)
            if m:
                increment = int(m.group(1))
                new_deck = [-1 for _ in range(len(deck))]
                cnt = 0
                for i, c in enumerate(deck):
                    new_deck[(cnt * increment) % len(deck)] = c
                    cnt += 1
                deck = new_deck
            m = re.match(r'cut (-?\d+)', l)
            if m:
                cut = int(m.group(1))
                deck = deck[cut:] + deck[:cut]
    return deck


print(run('22.test', list(range(10))))
print(run('22.test.2', list(range(10))))
print(run('22.test.3', list(range(10))))
print(run('22.test.4', list(range(10))))
deck = run('22.in', list(range(10007)))
for i, c in enumerate(deck):
    if c == 2019:
        print('part1', i)

deck = list(range(119315717514047))
for i in range(101741582076661):
    deck = run('22.in', deck)
print('part2', deck[2020])
