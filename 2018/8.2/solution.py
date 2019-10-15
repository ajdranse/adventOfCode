def parse(array, depth = 0):
    num_children = array[0]
    num_metadata = array[1]

    array = array[2:]

    child_values = []
    for i in xrange(num_children):
        (array, child_value) = parse(array, depth + 1)
        child_values.append(child_value)

    value = 0
    if num_children > 0:
        for i in xrange(num_metadata):
            index = array[0]
            if index > 0 and index <= num_children:
                value += child_values[index-1]
            array = array[1:]
    else:
        for i in xrange(num_metadata):
            value += array[0]
            array = array[1:]

    return (array, value)


array = []
with open('input') as f:
    for line in f:
        line = line.rstrip()
        array = [int(x) for x in line.split(' ')]

(array, value) = parse(array)
print("Value of root: {}".format(value))
