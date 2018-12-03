import collections

twice = []
thrice = []
with open('input') as f:
    for line in f:
        line = line.rstrip()
        d = collections.defaultdict(int)
        for c in line:
            d[c] += 1
        for char,count in d.iteritems():
            if count == 2 and line not in twice:
                twice.append(line)
            if count == 3 and line not in thrice:
                thrice.append(line)


    print(len(twice) * len(thrice))
