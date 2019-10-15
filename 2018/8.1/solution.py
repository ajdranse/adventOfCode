def parse(array):
    num_children = array[0]
    num_metadata = array[1]

    array = array[2:]

    checksum = 0
    for i in xrange(num_children):
        (array, child_checksum) = parse(array)
        checksum += child_checksum

    for i in xrange(num_metadata):
        checksum += array[0]
        array = array[1:]

    return (array, checksum)


array = []
with open('input') as f:
    for line in f:
        line = line.rstrip()
        array = [int(x) for x in line.split(' ')]

(array, checksum) = parse(array)
print("Checksum: {}".format(checksum))
