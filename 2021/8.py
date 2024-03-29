from collections import defaultdict


with open('8.in') as f:
    lines = f.read().splitlines()

num_unique = 0
for line in lines:
    (signal, output) = line.split(' | ')
    for w in output.split():
        if len(w) == 2 or len(w) == 3 or len(w) == 4 or len(w) == 7:
            num_unique += 1
print('part 1:', num_unique)

total_total = 0
segments = defaultdict(str)
for line in lines:
    (signal, output) = line.split(' | ')
    signals = signal.split()

    len_to_signal = defaultdict(list)
    to_num = defaultdict(int)

    for s in signals:
        len_to_signal[len(s)].append(s)

    to_num[len_to_signal[2][0]] = 1
    to_num[len_to_signal[3][0]] = 7
    to_num[len_to_signal[4][0]] = 4
    to_num[len_to_signal[7][0]] = 8

    # figuring out a
    # character in 7 not in 1
    num1 = len_to_signal[2][0]
    num7 = len_to_signal[3][0]
    for c in num1:
        num7 = num7.replace(c, '')
    segments['a'] = num7

    # figure out 3
    # one sharing c and f with 1
    num3 = None
    cs = num1
    for w in len_to_signal[5]:
        if all([c in w for c in cs]):
            to_num[w] = 3
            num3 = w
            break

    # figure out b
    # character in 4 that's not in 3
    num4 = len_to_signal[4][0]
    for c in num4:
        if c not in num3:
            segments['b'] = c
            break

    # figure out d
    # character in 4 that isn't b and isn't in 1
    for c in num4:
        if c != segments['b'] and c not in num1:
            segments['d'] = c
            break

    # figure out 5
    # contains b, d, and one character from 1
    for w in len_to_signal[5]:
        if segments['b'] in w and segments['d'] in w:
            matched = [c in w for c in num1]
            if any(matched) and not all(matched):
                to_num[w] = 5
                # figure out f (the shared char with 1)
                # figure out c (the other char in 1)
                for c in num1:
                    if c in w:
                        segments['f'] = c
                    else:
                        segments['c'] = c
                break

    # figure out 2
    for w in len_to_signal[5]:
        if w not in to_num.keys():
            to_num[w] = 2
            break

    # figure out e
    # 0, 6, 9 are missing d, c, and e respectively vs 8
    # we know d and c, so the len6 that's missing a char that's not d or c is 9 and that char is e
    num8 = len_to_signal[7][0]
    for w in len_to_signal[6]:
        for c in num8:
            if c not in w:
                if c == segments['d']:
                    to_num[w] = 0
                    break
                elif c == segments['c']:
                    to_num[w] = 6
                    break
                else:
                    to_num[w] = 9
                    segments['e'] = c
                    break

    total = 0
    for w in output.split(' '):
        total *= 10
        for n, t in to_num.items():
            if len(w) == len(n) and all([c in n for c in w]):
                total += t
                break
    total_total += total
print('part 2:', total_total)
