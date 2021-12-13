from collections import defaultdict


def traverse(graph, node, seen, part2, small):
    if node == 'end':
        return 1

    if node == 'start' and node in seen:
        return 0

    if node.islower() and node in seen:
        if part2 and small is None:
            small = node
        else:
            return 0

    seen = seen.copy()
    seen.add(node)

    paths = 0
    for n in graph[node]:
        ret = traverse(graph, n, seen, part2, small)
        paths += ret
    return paths


lines = [
'start-A',
'start-b',
'A-c',
'A-b',
'b-d',
'A-end',
'b-end',
]

with open('12.in') as f:
   lines = f.read().splitlines();

graph = defaultdict(list)
for l in lines:
    (start, end) = l.split('-')
    graph[start].append(end)
    graph[end].append(start)

paths = traverse(graph, 'start', set(), False, None)
print(f'part1: {paths}')
paths = traverse(graph, 'start', set(), True, None)
print(f'part1: {paths}')
