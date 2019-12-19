from itertools import permutations


def run(filename):
    g = {}
    all_nodes = set()
    with open(filename) as f:
        line = f.readline().strip()
        while line:
            des, dist = line.split(' = ')
            start, end = des.split(' to ')
            all_nodes.add(start)
            all_nodes.add(end)
            g[(start, end)] = int(dist)
            g[(end, start)] = int(dist)
            line = f.readline().strip()

    paths = permutations(all_nodes)
    min_path = None
    min_cost = None

    max_path = None
    max_cost = 0

    for path in paths:
        print(path)
        pairs = list(zip(path, path[1:]))
        cost = 0
        for p in pairs:
            cost += g[p]
        if not min_cost or cost < min_cost:
            min_cost = cost
            min_path = path
        if cost > max_cost:
            max_cost = cost
            max_path = path
    print(min_path, min_cost)
    print(max_path, max_cost)

# run('9.test')
run('9.in')
