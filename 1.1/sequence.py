with open('input') as f:
    array = []
    for line in f:
        array.append(int(line))

output = sum(array)
print(output)
