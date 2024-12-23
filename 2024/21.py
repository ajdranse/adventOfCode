import networkx
from itertools import product
from collections import defaultdict, Counter
from math import inf

NUMPAD = networkx.DiGraph()
NUMPAD.add_edge('A', '0', d='<')
NUMPAD.add_edge('A', '3', d='^')
NUMPAD.add_edge('0', 'A', d='>')
NUMPAD.add_edge('0', '2', d='^')
NUMPAD.add_edge('3', 'A', d='v')
NUMPAD.add_edge('3', '2', d='<')
NUMPAD.add_edge('3', '6', d='^')
NUMPAD.add_edge('2', '0', d='v')
NUMPAD.add_edge('2', '3', d='>')
NUMPAD.add_edge('2', '1', d='<')
NUMPAD.add_edge('2', '5', d='^')
NUMPAD.add_edge('1', '2', d='>')
NUMPAD.add_edge('1', '4', d='^')
NUMPAD.add_edge('4', '1', d='v')
NUMPAD.add_edge('4', '7', d='^')
NUMPAD.add_edge('4', '5', d='>')
NUMPAD.add_edge('5', '2', d='v')
NUMPAD.add_edge('5', '4', d='<')
NUMPAD.add_edge('5', '8', d='^')
NUMPAD.add_edge('5', '6', d='>')
NUMPAD.add_edge('6', '3', d='v')
NUMPAD.add_edge('6', '5', d='<')
NUMPAD.add_edge('6', '9', d='^')
NUMPAD.add_edge('7', '4', d='v')
NUMPAD.add_edge('7', '8', d='>')
NUMPAD.add_edge('8', '5', d='v')
NUMPAD.add_edge('8', '7', d='<')
NUMPAD.add_edge('8', '9', d='>')
NUMPAD.add_edge('9', '6', d='v')
NUMPAD.add_edge('9', '8', d='<')

# from -> to -> iterated
DIR_MAP = {
    'A': {'^': '<A', 'v': '<vA', '<': 'v<<A', '>': 'vA', 'A': 'A' },
    '^': {'^': 'A', 'v': 'vA', '<': 'v<A', '>': 'v>A', 'A': '>A' },
    '<':{'^': '>^A', 'v': '>A', '<': 'A', '>': '>>A', 'A': '>>^A' },
    'v':{'^': '^A', 'v': 'A', '<': '<A', '>': '>A', 'A': '^>A' },
    '>':{'^': '<^A', 'v': '<A', '<': '<<A', '>': 'A', 'A': '^A' }
}

def get_keypad_paths(path, keypad):
    # magic
    return [
        [
            ''.join([keypad.get_edge_data(p[idx], p[idx+1])['d'] for idx in range(len(p) - 1)]) + 'A'
            for p in networkx.all_shortest_paths(keypad, 'A' if idx == 0 else path[idx-1], path[idx])
        ]
        for idx in range(len(path))
    ]

def transform(part):
    n = []
    prev = 'A'
    for s in part:
        to_add = DIR_MAP[prev][s]
        n.append(to_add)
        prev = s
    return n

def get_len(p, depth):
    uniq = Counter(p)
    for x in range(depth):
        ret = defaultdict(int)
        for u, c in uniq.items():
            for t in transform(u):
                ret[t] += c
        uniq = ret
    return sum([len(k) * v for k, v in uniq.items()])

def run(depth):
    with open('21.in') as f:
        inp = [x.strip() for x in f.readlines()]

    complexity = 0
    for code in inp:
        min_len = min([get_len(p, depth) for p in product(*get_keypad_paths(code, NUMPAD))])
        intcode = int(''.join(c for c in code if c.isdigit()))
        complexity += min_len * intcode
    return complexity

if __name__ == '__main__':
    print('part1:', run(2))
    print('part2:', run(25))
