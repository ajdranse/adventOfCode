import sys
from sets import Set

seen = Set()
frequency = 0
iteration = 0
while True:
    print("iteration {}, running sum {}".format(iteration, frequency))
    with open('input') as f:
        for line in f:
            frequency += int(line)
            if frequency in seen:
                print(frequency)
                sys.exit(0)
            else:
                seen.add(frequency)
    iteration += 1
