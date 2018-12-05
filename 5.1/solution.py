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
            polymerChain.append(c)

iterations = 0
removed = removeOpposite()
while removed:
    removed = removeOpposite()
    iterations += 1
    if iterations % 100 == 0:
        print("{} iterations, length of chain is: {}".format(iterations, len(polymerChain)))

print(len(polymerChain))
