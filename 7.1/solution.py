import re

import networkx

pattern = re.compile(r'Step (.) must be finished before step (.) can begin.')
g = networkx.DiGraph()
with open('input') as f:
    for line in f:
        line = line.rstrip()
        m = re.match(pattern, line)
        if m:
            prereq = m.group(1)
            then = m.group(2)
            g.add_edge(prereq, then)
print(''.join(networkx.lexicographical_topological_sort(g)))
