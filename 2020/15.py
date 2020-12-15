for target in [2020, 30000000]:
    last = {20:0, 0:1, 1:2, 11:3, 6:4, 3:5}
    last_num = None
    num_spoken = len(last)
    while num_spoken < target:
        if last_num not in last:
            cur_num = 0
        else:
            cur_num = (num_spoken-1)-last[last_num]
        last[last_num] = num_spoken - 1
        last_num = cur_num
        num_spoken += 1
    print(last_num)
