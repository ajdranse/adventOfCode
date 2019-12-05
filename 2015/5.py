from collections import Counter

inp = []
with open('5.in') as f:
    inp = f.read().splitlines()
# inp = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']


bad = ['ab', 'cd', 'pq', 'xy']
nice = []
for string in inp:
    has_bad = any([b in string for b in bad])
    counted = Counter(string)
    vowel_count = counted['a'] + counted['e'] + counted['i'] + counted['o'] + counted['u']
    doubled = False
    for i, s in enumerate(string):
        if i < len(string) - 1 and string[i] == string[i+1]:
            doubled = True

    if not has_bad and vowel_count >= 3 and doubled:
        nice.append(string)

print('part 1: {}'.format(len(nice)))

# inp = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']

nice = []
for string in inp:
    repeat = False
    doubled_pair = False
    for i, s in enumerate(string):
        if not repeat and i < len(string) - 2:
            if string[i] == string[i+2]:
                repeat = True
        if not doubled_pair and i < len(string) - 1:
            pair = string[i:i+2]
            for j in range(i+2, len(string)):
                candidate = string[j:j+2]
                if pair == candidate:
                    doubled_pair = True
        if repeat and doubled_pair:
            nice.append(string)
            break
print('part 2: {}'.format(len(nice)))
