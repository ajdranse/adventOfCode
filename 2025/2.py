ranges = []
with open('2.in') as f:
    for x in f.readline().strip().split(','):
        a, b = x.split('-')
        ranges.append((a, b))

p1 = 0
p2 = set()
for r in ranges:
    for x in range(int(r[0]), int(r[1])+1):
        xs = str(x)
        for l in range(1, len(xs)+1):
            if len(xs) % l != 0:
                continue

            sp = [xs[a:a+l] for a in range(0, len(xs), l)]
            if len(sp) > 1 and sp.count(sp[0]) == len(sp):
                if len(sp) == 2:
                    p1 += x
                p2.add(x)
p2 = sum(p2)
print(f'{p1=}, {p2=}')
