import networkx

def solve(filename):
    regex = open(filename).read()[1:-2]
    print regex

    x = 0
    y = 0
    stack = []
    facility = networkx.Graph()
    for c in regex:
        if c == '|':
            # end branch
            x, y = stack[-1]
        elif c in 'NESW':
            # move
            x_dir = 0
            y_dir = 0
            if c == 'N':
                y_dir = 1
            elif c == 'E':
                x_dir = 1
            elif c == 'S':
                y_dir = -1
            elif c == 'W':
                x_dir = -1

            cur_pos = x, y
            x += x_dir
            y += y_dir
            new_pos = x, y
            facility.add_edge(cur_pos, new_pos)
        elif c == '(':
            # start branches
            stack.append((x, y))
        elif c == ')':
            # end all branches
            x, y = stack.pop()

    all_distances = networkx.algorithms.shortest_path_length(facility, (0, 0))
    print("part1: {}".format(max(d for d in all_distances.values())))
    print("part2: {}".format(len([d for d in all_distances.values() if d >= 1000])))

#solve('test')
#solve('test1')
#solve('test2')
#solve('test3')
#solve('test4')
solve('input')
