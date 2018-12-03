import sys

array = []
with open('input') as f:
    for line in f:
        line = line.rstrip()
        array.append(line)

for i in array:
    for j in array:
        differing = 0
        common = []
        for c in range(0, len(i)):
            if i[c] != j[c]:
                differing += 1
            else:
                common.append(i[c])
            if differing > 1:
                next
        if differing == 1:
            print(''.join(common))
            sys.exit(0)
