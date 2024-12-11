import re


def findfile(disk, file_id):
    start_idx = None
    for i in range(len(disk)):
        if disk[i] == file_id and start_idx is None:
            start_idx = i
        if start_idx is not None and disk[i] != file_id:
            return (start_idx, i)
    return (start_idx, len(disk))

def lastdigit(disk, start = None):
    if start == None:
        start = len(disk)

    start_idx = None
    for i in range(start-1, 0, -1):
        if disk[i] != '.' and start_idx is None:
            start_idx = i
        if start_idx is not None:
            if disk[i] == '.' or (part2 and disk[i] != disk[start_idx]):
                return (start_idx, i)
    return (start_idx, 0)

def firstempty(disk, start = 0):
    start_idx = None
    for i in range(start, len(disk)):
        if disk[i] == '.' and start_idx is None:
            start_idx = i
        if disk[i] != '.' and start_idx is not None:
            return (start_idx, i)
    return (start_idx, len(disk) - 1)

def gaps(disk):
    e = firstempty(disk)[0]
    d = lastdigit(disk)[0]
    return e is not None and e < d

def checksum(disk):
    cs = 0
    for idx, x in enumerate(disk):
        if x != '.':
            cs += (idx * x)
    return cs

def part1(disk):
    iterations = 0
    while gaps(disk):
        (last_digit_end_idx, last_digit_start_idx) = lastdigit(disk)
        (first_empty_start_idx, first_empty_end_idx) = firstempty(disk)
        # if iterations % 10 == 0:
        #     print(iterations)
        #     print('last digits: ', last_digit_start_idx, last_digit_end_idx, disk[last_digit_start_idx+1:last_digit_end_idx])
        #     print('first empty: ', first_empty_start_idx, first_empty_end_idx, disk[first_empty_start_idx:first_empty_end_idx-1])

        length = min((last_digit_end_idx - last_digit_start_idx), (first_empty_end_idx - first_empty_start_idx))
        disk[first_empty_start_idx:first_empty_start_idx + length] = disk[last_digit_end_idx:last_digit_end_idx - length:-1]
        disk = disk[:last_digit_end_idx - length + 1]
        # print(disk)
        iterations += 1

    print('part1:', checksum(disk))

def part2(disk):
    next_file_id = int(disk[-1])
    while next_file_id >= 0:
        # print(f'{next_file_id=}')
        (file_start, file_end) = findfile(disk, next_file_id)
        file_len = file_end - file_start
        # print(f'{next_file_id=}, {file_len=}, {file_start=}, {file_end=}')
        empty_block_start = 0
        empty_block_end = 0
        while True:
            (empty_block_start, empty_block_end) = firstempty(disk, empty_block_end)
            if empty_block_start is None or empty_block_start == len(disk) - 1 or empty_block_start > file_start:
                break
            empty_block_len = empty_block_end - empty_block_start
            if empty_block_len >= file_len:
                disk[empty_block_start:empty_block_start + file_len] = disk[file_start:file_end]
                disk[file_start:file_end] = ['.'] * file_len
                break
        next_file_id -= 1
    print('part2:', checksum(disk))

def parse():
    with open('9.in') as f:
        inp = [x.strip() for x in f.readlines()]
        inp = [int(c) for c in inp[0]]

    # print(inp)

    file = True
    disk = []
    file_id = 0
    for b in inp:
        if file:
            disk.extend([file_id] * b)
            file = False
            file_id += 1
        else:
            file = True
            disk.extend(['.'] * b)
    return disk

if __name__ == '__main__':
    disk = parse()
    part1(disk.copy())
    part2(disk.copy())
