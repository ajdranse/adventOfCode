elves = []
max_idx = -1
max_cnt = -1
with open('1.in') as f:
    cnt = 0
    for l in f.readlines():
        l = l.strip()
        if l == '':
            if cnt > max_cnt:
                max_idx = len(elves)
                max_cnt = cnt
            elves.append(cnt)
            cnt = 0
        else:
            cnt += int(l)
    print(max_idx, max_cnt)
    elves.sort(reverse=True)
    print(sum(elves[0:3]))
