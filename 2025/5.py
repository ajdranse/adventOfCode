def merge(fresh):
    fresh = sorted(fresh)
    merged = []
    cur = fresh[0]
    for idx in range(1, len(fresh)):
        f = fresh[idx]
        if f[0] - cur[1] <= 1:
            cur = (cur[0], max(cur[1], f[1]))
        else:
            merged.append(cur)
            cur = f
    merged.append(cur)
    return merged


fresh = []
candidates = []
with open('5.in') as f:
    for line in f.readlines():
        line = line.strip()
        if line == '':
            pass
        elif '-' in line:
            s, e = line.split('-')
            fresh.append((int(s), int(e)))
        else:
            i = int(line)
            candidates.append(i)
candidates = sorted(candidates)
fresh = merge(fresh)

p1 = 0
for c in candidates:
    for (s, e) in fresh:
        if c >= s and c <= e:
            p1 += 1
            break
print(f'p1={p1}')

p2 = sum([e - s + 1 for (s, e) in fresh])
print(f'{p2=}')
