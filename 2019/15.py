import networkx as nx
from collections import defaultdict
from queue import Queue
from intcode import print_grid, IntCode
import time
import random

inq = Queue()
outq = Queue()
grid = defaultdict(int)
grid_values = {0: ' ', 1: '#', 2: '.', 3: 'D', 4: 'O'}
DX = {1: 0, 2: 0, 3: 1, 4: -1}
DY = {1: -1, 2: 1, 3: 0, 4: 0}
moves = []

def fill():
    minutes = 0
    while sum([1 for x, y in grid.keys() if grid.get((x, y)) == 2]):
        minutes += 1
        already_filled = [(x, y) for (x, y) in grid.keys() if grid.get((x, y)) == 4]
        for p in already_filled:
            for i in range(1, 5):
                if grid.get((p[0] + DX[i], p[1] + DY[i])) == 2:
                    grid[(p[0] + DX[i], p[1] + DY[i])] = 4
        # print_grid(grid, grid_values)
    print('done after ', minutes)


def find_path_to(pos):
    g = nx.DiGraph()
    max = 0
    for x, y in grid.keys():
        if grid.get((x, y)) in [0, 1]:
            continue
        if grid.get((x-1, y)) in [4, 3, 2]:
            g.add_edge((x, y), (x-1, y))
        if grid.get((x+1, y)) in [4, 3, 2]:
            g.add_edge((x, y), (x+1, y))
        if grid.get((x, y-1)) in [4, 3, 2]:
            g.add_edge((x, y), (x, y-1))
        if grid.get((x, y+1)) in [4, 3, 2]:
            g.add_edge((x, y), (x, y+1))
    path = nx.dijkstra_path(g, (0, 0), pos)
    print(path)
    print(len(path) - 1)

with open('15.in') as f:
    memory = [int(x.strip()) for x in f.read().split(',')]
    t = IntCode(memory.copy(), inq, outq)
    t.start()
    unexplored = {}
    moves = []
    pos = (0, 0)
    oxygen = None
    while True:
        if pos not in unexplored:
            unexplored[pos] = [1, 2, 3, 4]

        if len(unexplored[pos]) > 0:
            back = False
            move = unexplored[pos].pop()
        else:
            back = True
            if len(moves) == 0:
                # back at start
                print_grid(grid, grid_values)
                break
            prev = moves.pop()
            if prev == 1:
                move = 2
            if prev == 2:
                move = 1
            if prev == 3:
                move = 4
            if prev == 4:
                move = 3
        inq.put(move)
        res = outq.get()
        new_pos = pos[0] + DX[move], pos[1] + DY[move]
        if res == 0:
            grid[new_pos] = 1 # hit a wall in that direction
        elif res == 1:
            grid[new_pos] = 2
            if not back:
                moves.append(move)
            pos = new_pos
        elif res == 2:
            grid[new_pos] = 4
            if not back:
                oxygen = new_pos
                print('found oxygen at ', new_pos)
                moves.append(move)
            pos = new_pos

    find_path_to(oxygen)
    fill()
    # t.join()
