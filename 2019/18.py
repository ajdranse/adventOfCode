import networkx as nx
from collections import deque
from copy import deepcopy
from intcode import print_grid


def build_graph(grid, start):
    directions = [1, 2, 3, 4]
    DX = {1: 1, 2: -1, 3: 0, 4: 0}
    DY = {1: 0, 2: 0,  3: 1, 4: -1}
    g = nx.Graph()
    todo = deque([start])
    seen = set()
    while todo:
        cur = todo.popleft()
        if cur in seen:
            continue
        seen.add(cur)
        for i in directions:
            test_pos = (cur[0] + DX[i], cur[1] + DY[i])
            if test_pos in seen:
                continue
            if grid[test_pos] != '#':
                g.add_edge(cur, test_pos)
                todo.append(test_pos)
    return g


def build_paths(graph, keys):
    paths = {}
    for from_key, from_pos in keys.items():
        for to_key, to_pos in keys.items():
            if to_key == from_key:
                continue
            path = nx.shortest_path(graph, from_pos, to_pos)
            paths[(from_pos, to_pos)] = path
            paths[(to_pos, from_pos)] = list(reversed(path))
    return paths


def find_paths_2(states, grid, num_needed_keys):
    starts = tuple(s[0] for s in states)
    todo = deque([(starts, 0, ())])
    min_paths = []
    seen = {}
    while todo:
        at_positions, dist, have_keys = todo.popleft()
        # print('at: {} with keys {}'.format(at_positions, have_keys))
        if min_paths and dist >= min_paths[0][0]:
            # print('have a min path and this dist is already bigger than it, give up')
            continue
        if len(have_keys) == num_needed_keys:
            if not min_paths or dist < min_paths[0][0]:
                min_paths = []
                min_paths.append((dist, deepcopy(have_keys)))
                print('new min path with dist: {} key order {}', dist, have_keys)
            elif dist == min_paths[0][0]:
                min_paths.append((dist, deepcopy(have_keys)))
            else:
                print('found all keys, too long:', dist)
            continue
        key = (at_positions, ''.join(sorted(have_keys)))
        results = None
        if key in seen:
            old_dist, results = seen[key]
            if old_dist <= dist:
                # print('this key ({}) already seen, and with a lower distance'.format(key))
                continue
        else:
            results = []
            for i, at_pos in enumerate(at_positions):
                # print('finding next move for idx {} at {}'.format(i, at_pos))
                local_all_keys = states[i][2]
                local_paths = states[i][3]
                res = tuple(sorted(
                    find_accessible(at_pos, grid, have_keys, local_all_keys, local_paths), key=lambda r: r[2]))
                for r in res:
                    # print('got move:', r)
                    results.append((i, *r))
            # print('after looking at all bots, got:', results)
        seen[key] = dist, results
        for i, new_key, new_pos, new_dist in results:
            new_positions = at_positions[:i] + (new_pos, ) + at_positions[i+1:]
            todo.append((new_positions, dist + new_dist, have_keys + (new_key, )))

    return min_paths


def find_paths(start, grid, graph, paths, all_keys):
    todo = deque([(start, 0, ())])
    min_path = None
    seen = {}
    while todo:
        # if len(todo) % 100 == 0:
        #     print(len(todo))
        at_pos, dist, have_keys = todo.popleft()
        if min_path and dist >= min_path:
            continue
        if len(have_keys) == len(all_keys):
            if not min_path or dist < min_path:
                min_path = dist
                print('new min path with dist:', dist)
            else:
                print('found all keys, too long:', dist)
        key = (at_pos, ''.join(sorted(have_keys)))
        if key in seen:
            old_dist, res = seen[key]
            if old_dist <= dist:
                continue
        else:
            res = tuple(sorted(find_accessible(at_pos, grid, have_keys, all_keys, paths), key=lambda r: r[2]))
        seen[key] = dist, res
        for new_key, new_pos, new_dist in res:
            todo.append((new_pos, dist + new_dist, have_keys + (new_key, )))

    return min_path


def find_accessible(pos, grid, have_keys, all_keys, paths):
    accessible = []
    for needed, needed_pos in all_keys.items():
        if needed in have_keys:
            # print('already have {}'.format(needed))
            continue
        path = paths[(pos, needed_pos)]
        # print('path is {}'.format(path))
        okay = set([k.upper() for k in have_keys]) | set('.@' + ''.join(list(all_keys.keys())))
        # for p in path:
        #     if grid[p] not in okay:
        #         print('pos {} ({}) not in okay ({})'.format(p, grid[p], okay))
        if any(grid[p] not in okay for p in path):
            continue
        accessible.append((needed, all_keys[needed], len(path) - 1))
        # print('adding to accessible:', accessible)
    return accessible


def run(filename):
    # part1
    grid = {}
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        x = y = 0
        for l in lines:
            x = 0
            for c in l:
                grid[(x, y)] = c
                x += 1
            y += 1
    print_grid(grid, None)

    starts = tuple(pos for pos in grid if grid[pos] == '@')
    all_keys = {k: pos for pos, k in grid.items() if k in 'abcdefghijklmnopqrstuvwxyz'}

    print('starting at ', starts)
    print('need to get keys:', all_keys)

    all_keys['@'] = starts[0]
    graph = build_graph(grid, starts[0])
    all_paths = build_paths(graph, all_keys)
    del all_keys['@']
    min_dist = find_paths(starts[0], grid, graph, all_paths, all_keys)
    print(min_dist)


def run2(filename):
    # part2
    grid = {}
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        x = y = 0
        for l in lines:
            x = 0
            for c in l:
                grid[(x, y)] = c
                x += 1
            y += 1
    print_grid(grid, None)

    starts = tuple(pos for pos in grid if grid[pos] == '@')
    all_keys = {k: pos for pos, k in grid.items() if k in 'abcdefghijklmnopqrstuvwxyz'}

    print('starting at ', starts)
    print('need to get keys:', all_keys)

    states = []
    for s in starts:
        local_graph = build_graph(grid, s)
        local_all_keys = {k: v for k, v in all_keys.items() if v in local_graph.nodes}
        local_all_keys['@'] = s
        local_all_paths = build_paths(local_graph, local_all_keys)
        del local_all_keys['@']
        states.append([s, local_graph, local_all_keys, local_all_paths])
    paths = find_paths_2(states, grid, len(all_keys))
    print(min(p[0] for p in paths))


# part1
run('18.test')
run('18.test.2')
run('18.test.3')
run('18.test.4')
run('18.test.5')
print('part1')
run('18.in')
# part2
run2('18.test.6')
run2('18.test.7')
print('part2')
run2('18.in.2')
