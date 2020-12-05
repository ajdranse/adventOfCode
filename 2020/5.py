def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)


lines = []
with open("5.in") as f:
    for line in f:
        lines.append(line)

# tests = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
# for line in tests:
highest_id = 0
ids = []
for line in lines:
    # 1111111 = 127
    # 111 = 7
    row = 127
    row_bit = 6
    col = 7
    col_bit = 2
    for c in line:
        if c == 'F':
            row = clear_bit(row, row_bit)
            row_bit -= 1
            # print('row lower half, have: {}'.format(row))
        elif c == 'B':
            row = set_bit(row, row_bit)
            row_bit -= 1
            # print('row upper half, have: {}'.format(row))
        elif c == 'R':
            col = set_bit(col, col_bit)
            col_bit -= 1
            # print('col upper half, have: {}'.format(col))
        elif c == 'L':
            col = clear_bit(col, col_bit)
            col_bit -= 1
            # print('col lower half, have: {}'.format(col))

    id = (row*8) + col
    if id > highest_id:
        highest_id = id
    ids.append(id)
    # print(test, row, col, (row*8) + col)
print('part1: {}'.format(highest_id))
ordered_ids = list(dict.fromkeys(ids))
idx = 0
expected = ordered_ids[idx]
for i in ordered_ids:
    if ordered_ids[idx] != expected:
        print('part 2: {}'.format(expected))
        break
    idx += 1
    expected += 1
