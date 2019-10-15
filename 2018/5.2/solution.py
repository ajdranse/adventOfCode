startingChain = []
polymerChain = []

def removeOpposite():
    removed = False
    for idx in xrange(0, len(polymerChain) - 1):
        try:
            first = polymerChain[idx]
            second = polymerChain[idx+1]
            if first.lower() == second.lower():
                # same char
                if first != second:
                    # different case
                    del polymerChain[idx+1]
                    del polymerChain[idx]
                    removed = True

        except Exception, e:
            # hit end of array, just iterate again
            pass

    return removed

with open ('input') as f:
    for line in f:
        line = line.rstrip()
        for c in line:
            startingChain.append(c)

print("Starting length: {}".format(len(startingChain)))

minLength = len(startingChain)
bestChar = None
for c in 'abcdefghijklmnopqrstuvwxyz':
    polymerChain = [x for x in startingChain if x.lower() != c]
    print("Removed {} now length is {}".format(c, len(polymerChain)))
    removed = removeOpposite()
    while removed:
        removed = removeOpposite()

    if len(polymerChain) < minLength:
        bestChar = c
        minLength = len(polymerChain)

print("Best char to remove is: {} giving min length: {}".format(bestChar, minLength))
