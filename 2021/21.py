from collections import defaultdict


# Player 1 starting position: 6
# Player 2 starting position: 9

die = 1
p1 = 6
p2 = 9
p1_score = 0
p2_score = 0

rolls = 0
while True:
    # (p1 + die + die + 1 + die + 2 - 1) % 10 + 1 -> (p1 + (3 * die) + 3 - 1) % 10 + 1 -> (p1 + (3 * die) + 2) % 10 + 1
    p1 = (p1 + (3 * die) + 2) % 10 + 1
    die = (die + 2) % 100 + 1
    rolls += 3
    p1_score += p1

    if p1_score >= 1000:
        break

    p2 = (p2 + (3 * die) + 2) % 10 + 1
    die = (die + 2) % 100 + 1
    rolls += 3
    p2_score += p2

    if p2_score >= 1000:
        break

print('part1', min(p1_score, p2_score) * rolls)

cache = {}

def go(p1, p2, p1_score, p2_score, p):
    if (p1, p2, p1_score, p2_score, p) in cache.keys():
        return cache[(p1, p2, p1_score, p2_score, p)]

    # wins from this point
    p1_wins = 0
    p2_wins = 0

    # calculate all possible rolls
    for r in [a + b + c for a in [1, 2, 3] for b in [1, 2, 3] for c in [1, 2, 3]]:
        if p == 1:
            new_pos = (p1 + r - 1) % 10 + 1
            new_score = p1_score + new_pos
            if new_score >= 21:
                p1_wins += 1
            else:
                (from_here_1, from_here_2) = go(new_pos, p2, new_score, p2_score, 2)
                p1_wins += from_here_1
                p2_wins += from_here_2
        else:
            new_pos = (p2 + r - 1) % 10 + 1
            new_score= p2_score + new_pos
            if new_score >= 21:
                p2_wins += 1
            else:
                (from_here_1, from_here_2) = go(p1, new_pos, p1_score, new_score, 1)
                p1_wins += from_here_1
                p2_wins += from_here_2
    cache[(p1, p2, p1_score, p2_score, p)] = (p1_wins, p2_wins)
    return (p1_wins, p2_wins)

(p1, p2) = go(6, 9, 0, 0, 1)
print('part2', max(p1, p2))
