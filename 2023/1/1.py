import re


test = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet',
]
test2 = [
'two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen',
'kkdhmmvvmthreezxqzqmb4khprbldcr'
]

print('part 1')
with open('1.in') as f:
    ints = []
    for t in f.readlines():
        t = t.strip()
        n = re.sub(r'[a-z]*', '', t)
        ints.append(int(n[0] + n[-1]))

    print(sum(ints))

def findfirst(t):
    for idx in range(len(t)):
        if t[idx].isdigit():
            return int(t[idx])
        elif t[idx:idx+3] == 'one':
            return 1
        elif t[idx:idx+3] == 'two':
            return 2
        elif t[idx:idx+5] == 'three':
            return 3
        elif t[idx:idx+4] == 'four':
            return 4
        elif t[idx:idx+4] == 'five':
            return 5
        elif t[idx:idx+3] == 'six':
            return 6
        elif t[idx:idx+5] == 'seven':
            return 7
        elif t[idx:idx+5] == 'eight':
            return 8
        elif t[idx:idx+4] == 'nine':
            return 9
    raise Exception('error')

def findlast(t):
    for idx in range(len(t) - 1, -1, -1):
        if t[idx].isdigit():
            return int(t[idx])
        elif t[idx-2:idx+1] == 'one':
            return 1
        elif t[idx-2:idx+1] == 'two':
            return 2
        elif t[idx-4:idx+1] == 'three':
            return 3
        elif t[idx-3:idx+1] == 'four':
            return 4
        elif t[idx-3:idx+1] == 'five':
            return 5
        elif t[idx-2:idx+1] == 'six':
            return 6
        elif t[idx-4:idx+1] == 'seven':
            return 7
        elif t[idx-4:idx+1] == 'eight':
            return 8
        elif t[idx-3:idx+1] == 'nine':
            return 9
    raise Exception('error')

print('part 2')
with open('1.in') as f:
    ints = []
    for t in f.readlines():
        t = t.strip()
        first = findfirst(t)
        last = findlast(t)
        newint = int(str(first) + str(last))
        print(t, first, last, newint)
        ints.append(newint)
    print(sum(ints))
