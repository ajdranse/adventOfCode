from collections import defaultdict

array = []
with open('input') as f:
    for line in f:
        line = line.rstrip()
        tup = tuple(int(x) for x in line.split(','))
        array.append(tup)

total_width = max(zip(*array)[0])
total_height = max(zip(*array)[1])

min_x = 0
max_x = total_width
min_y = 0
max_y = total_height

size = 0
for i in range(min_x, max_x):
    for j in range(min_y, max_y):
        loc = (i, j)
        total_distance = 0
        for a in array:
            total_distance += (abs(a[0] - loc[0]) + abs(a[1] - loc[1]))
        if total_distance < 10000:
            size += 1
print(size)
