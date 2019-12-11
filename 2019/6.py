from anytree import Node, Walker, search


def build_tree(root, nodes, orbits):
    orbiters = orbits.get(root.name, [])
    for orbiter in orbiters:
        cur = Node(orbiter, parent=root)
        nodes.append(cur)
        build_tree(cur, nodes, orbits)


root = Node('COM')
orbits = {}
with open('6.in') as f:
    for x in f.read().splitlines():
        # AAA)BBB = BBB is in orbit around AAA
        orbit = x.split(')')
        if orbit[0] not in orbits:
            orbits[orbit[0]] = [orbit[1]]
        else:
            orbits[orbit[0]].append(orbit[1])

nodes = []
build_tree(root, nodes, orbits)

length = 0
w = Walker()
for node in nodes:
    length += len(w.walk(node, root)[0])
print('part 1: {}'.format(length))

you = search.find(root, lambda node: node.name == 'YOU')
san = search.find(root, lambda node: node.name == 'SAN')

res = w.walk(you, san)
print('part 2: {}'.format(len(res[0]) + len(res[2]) - 2))
