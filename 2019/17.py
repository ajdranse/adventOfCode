import networkx as nx
from collections import defaultdict
from queue import Queue
from intcode import print_grid, IntCode
import time
import random

test = '..#..........\n..#..........\n#######...###\n#.#...#...#.#\n#############\n..#...#...#..\n..#####...^..'

def to_grid(inp):
    grid = {}
    x = 0
    y = 0
    for i, c in enumerate(inp):
        if c == '\n':
            y += 1
            x = 0
        else:
            grid[(x, y)] = c
            x += 1
    print(inp)
    return grid

def get_opposite(d):
    if d == 'v':
        return '^'
    elif d == '^':
        return 'v'
    elif d == '<':
        return '>'
    elif d == '>':
        return '<'

DX = {'^': 0, 'v': 0, '>': 1, '<': -1}
DY = {'^': -1, 'v': 1, '>': 0, '<': 0}
seen = []

def get_turn(old_d, new_d):
    if old_d == '^':
        if new_d == '>':
            return 'R'
        elif new_d == '<':
            return 'L'
    elif old_d == 'v':
        if new_d == '>':
            return 'L'
        elif new_d == '<':
            return 'R'
    elif old_d == '<':
        if new_d == '^':
            return 'R'
        elif new_d == 'v':
            return 'L'
    elif old_d == '>':
        if new_d == '^':
            return 'L'
        elif new_d == 'v':
            return 'R'


def find_intersections(grid, pos, direction):
    intersections = []
    moves = []
    while True:
        prev_pos = None
        length = 0
        while grid.get(pos, None) and grid[pos] == '#':
            if pos in seen:
                intersections.append(pos)
            else:
                seen.append(pos)
            prev_pos = pos
            pos = (pos[0] + DX[direction], pos[1] + DY[direction])
            length += 1
        if length:
            moves.append(length)
        if prev_pos:
            pos = prev_pos
        for i in DX.keys():
            if i != get_opposite(direction):
                test_pos = (pos[0] + DX[i], pos[1] + DY[i])
                if grid.get(test_pos) and grid[test_pos] == '#':
                    moves.append(get_turn(direction, i))
                    direction = i
                    pos = test_pos
                    break
        else:
            break
    print(intersections)
    print(moves)
    return intersections

with open('17.in') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    inq = Queue()
    outq = Queue()
    t = IntCode(memory.copy(), inq, outq)
    t.start()
    raw_grid = []
    while t.is_alive():
        raw_grid.append(outq.get())
    grid_len = len(raw_grid)
    t.join()
    scaffolds = ''.join([str(chr(x)) for x in raw_grid])
    grid = to_grid(scaffolds)
    # grid = to_grid(test)
    robot_pos = None
    for (x, y), c in grid.items():
        if c in ['v', '^', '<', '>']:
            robot_pos = (x, y)
            break
    print('robot at ', robot_pos)
    intersections = find_intersections(grid, robot_pos, grid[robot_pos])
    print('part1: ', sum(i[0] * i[1] for i in intersections))

    # A = ['R', 6, 'L', 12, 'R', 6]
    A = [82, 44, 54, 44, 76, 44, 49, 50, 44, 82, 44, 54, 10]
    # B = ['L', 12, R, 6, L, 8, L, 12]
    B = [76, 44, 49, 50, 44, 82, 44, 54, 44, 76, 44, 56, 44, 76, 44, 49, 50, 10]
    # C = [R, 12, L, 10, L, 10]
    C = [82, 44, 49, 50, 44, 76, 44, 49, 48, 44, 76, 44, 49, 48, 10]
    #main_routine =[A,      A,      B,      C,      B,      C,      B,      C,      B,      A]
    main_routine = [65, 44, 65, 44, 66, 44, 67, 44, 66, 44, 67, 44, 66, 44, 67, 44, 66, 44, 65, 10]

    part2 = memory.copy()
    part2[0] = 2
    inq = Queue()
    outq = Queue()
    t = IntCode(part2, inq, outq)
    t.start()
    s = ''
    for i in main_routine:
        s += str(chr(i))
        inq.put(i)
    print('main: ', s)
    s = ''
    for i in A:
        s += str(chr(i))
        inq.put(i)
    print('A: ', s)
    s = ''
    for i in B:
        s += str(chr(i))
        inq.put(i)
    print('B: ', s)
    s = ''
    for i in C:
        s += str(chr(i))
        inq.put(i)
    print('C: ', s)
    s = ''
    inq.put(110)
    # inq.put(121)
    inq.put(10)

    # raw_grid = []
    # while t.is_alive():
    #     raw_grid.append(outq.get())
    #     if len(raw_grid) == grid_len:
    #         print(''.join([str(chr(x)) for x in raw_grid]))
    #         raw_grid = []

    t.join()
    while not outq.empty():
        dust = outq.get()
    print('part2:', dust)
