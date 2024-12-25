import copy
import random

from collections import defaultdict
from itertools import combinations, product


def do(a, op, b):
    if op == 'AND':
        return a & b
    elif op == 'OR':
        return a | b
    elif op == 'XOR':
        return a ^ b

def part1(wires):
    done = False
    prev = len([v for v in wires.values() if type(v) == tuple])
    while not done:
        new_wires = copy.deepcopy(wires)
        for c, v in wires.items():
            if type(v) == tuple:
                a, op, b = v
                if type(wires[a]) == int and type(wires[b]) == int:
                    new_wires[c] = do(wires[a], op, wires[b])
        done = all([type(v) == int for v in new_wires.values()])
        wires = new_wires

        # bail out if we're stuck
        cur = len([v for v in wires.values() if type(v) == tuple])
        if cur == prev:
            return None
        prev = cur

    max_z = max([int(w[1:]) for w in wires.keys() if w.startswith('z')])
    out = [0 for _ in range(max_z + 1)]
    for k in wires.keys():
        if k.startswith('z'):
            out[len(out) - int(k[1:]) - 1] = wires[k]

    outval = int(''.join([str(o) for o in out]), 2)
    return outval

def part2(wires):
    # manual analysis of wtf this is
    # adders suck
    # all zXX are result of XOR
      # except the last one (45)
    # all XORS should have xXX, yXX as inputs or zXX as output
    # all OR inputs should be outputs of ANDs and vice-versa
    # so let's identify the ones that don't match this
    or_inps = set()
    and_outps = set()
    suspect = set()
    for k, v in wires.items():
        if type(v) == int:
            continue

        a, op, b = v
        if k[0] == 'z' and op != 'XOR' and k != 'z45':
            print(k, v, 'zXX not result of XOR')
            suspect.add(k)
        if op == 'XOR':
            if not (((a[0] == 'x' and b[0] == 'y') or (a[0] == 'y' and b[0] == 'x')) or k[0] == 'z'):
                print(k, v, 'XOR not x/y inp or z outp')
                suspect.add(k)
        if op == 'OR':
            or_inps.add(a)
            or_inps.add(b)
        if op == 'AND' and a != 'x00' and b != 'y00':
            and_outps.add(k)
    for x in or_inps.symmetric_difference(and_outps):
        print(x, 'OR inputs not AND output or vice-versa')
        suspect.add(x)
    if len(suspect) != 8:
        raise ValueError(suspect)
    return ','.join(sorted(suspect))


def parse():
    with open('24.in') as f:
        inp = [x.strip() for x in f.readlines()]

    wires = {}
    for l in inp:
        if ':' in l:
            wire, val = l.split(': ')
            wires[wire] = int(val)
        if '->' in l:
            a, op, b = l.split('->')[0].split()
            c = l.split('-> ')[1]
            wires[c] = (a, op, b)
    return wires

if __name__ == '__main__':
    wires = parse()
    print('part1:', part1(wires))

    wires = parse()
    print('part2:', part2(wires))
