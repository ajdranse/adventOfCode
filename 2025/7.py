import networkx as nx

def p1(rows, beams):
    splits = 0
    for idx, splitters in enumerate(rows):
        for s in splitters:
            new_beams = set()
            for b in beams:
                if b == s:
                    # split
                    splits += 1
                    new_beams.add(s-1)
                    new_beams.add(s+1)
                else:
                    new_beams.add(b)
            beams = list(new_beams)
        print(f'{idx} {beams=}')
    print(splits)


def p2_g(width, rows, beams):
    G = nx.DiGraph()
    print(f'root {(0, beams[0])}')
    root = (0, beams[0])
    G.add_node(root)

    for idx in range(1, len(rows)):
        splitters = rows[idx]
        print(f'Row: {idx}')
        if len(splitters) == 0:
            for b in beams:
                print(f'No splitters, straight down, edge from {(idx-1, b)} to {(idx, b)}')
                G.add_edge((idx-1, b), (idx, b))
        else:
            new_beams = set()
            for b in beams:
                if b in splitters:
                    # split
                    print(f'Split, edge from {(idx-1, b)} to {(idx, b-1)}')
                    G.add_edge((idx-1, b), (idx, b-1))
                    print(f'Split, edge from {(idx-1, b)} to {(idx, b+1)}')
                    G.add_edge((idx-1, b), (idx, b+1))
                    new_beams.add(b-1)
                    new_beams.add(b+1)
                else:
                    # straight down
                    print(f'Straight down, edge from {(idx-1, b)} to {(idx, b)}')
                    G.add_edge((idx-1, b), (idx, b))
                    new_beams.add(b)
            beams = list(new_beams)
            print(f'{idx}, {beams=}')
    np = 0
    for x in range(width):
        print(f'Paths to {x}:')
        paths = list(nx.all_simple_paths(G, root, (15, x)))
        np += len(paths)
        print(len(paths))
    print(np)



def p2(rows, beams):
    p2_g(rows, beams)
    raise ValueError
    beams = [(b,) for b in beams]

    print(len(rows))
    for idx, splitters in enumerate(rows):
        for s in splitters:
            new_beams = set()
            for b in beams:
                if b[-1] == s:
                    new_beams.add((*b, s-1))
                    new_beams.add((*b, s+1))
                else:
                    new_beams.add(b)
            beams = list(new_beams)
        print(f'{idx} {len(beams)}')
    print(len(beams))


with open('7.in') as f:
    lines = [x.strip() for x in f.readlines()]

beams = []
rows = []
for l in lines:
    cur = []
    for idx, c in enumerate(l):
        if c == 'S':
            beams.append(idx)
        elif c == '^':
            cur.append(idx)

    rows.append(cur)
print(beams, rows)
p1(rows, beams)

width = len(lines[0])
p2_g(width, rows, beams)
