import re
import networkx as nx


def get_bags(G, node):
    edges = G.edges(node, data=True)
    bags = 1 # this bag counts
    for e in edges:
        bags += (int(e[2]['weight']) * get_bags(G, e[1]))
    return bags


G = nx.DiGraph()
colours = set()
# with open("7.test") as f:
# with open("7.test2") as f:
with open("7.in") as f:
    for line in f:
        m = re.search('(.*) bags contain (.*)', line)
        key = m.group(1)
        colours.add(key)
        G.add_node(key)
        contains = m.group(2)
        if contains != 'no other bags.':
            split = contains.split(',')
            for v in split:
                m = re.search('(\d+) (.*) bag.?', v)
                count = m.group(1)
                colour = m.group(2)
                colours.add(colour)
                G.add_node(colour)
                G.add_edge(key, colour, weight=count)

can_contain = 0
for c in colours:
    if c != 'shiny gold':
        try:
            paths = list(nx.shortest_simple_paths(G, c, 'shiny gold'))
            can_contain += 1
        except nx.NetworkXNoPath:
            pass
print('part 1: {}'.format(can_contain))
print('part 2: {}'.format(get_bags(G, 'shiny gold') - 1))  # subtract the shiny gold bag
