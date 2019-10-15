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

print("Task order: {}".format(''.join(networkx.lexicographical_topological_sort(g))))
taken_tasks = {}
#taken_tasks = []
#taken_tasks_time_left = []
total_time = 0
while taken_tasks or g:
    # available tasks are those that are not already available and have no ancestors
    available_tasks = [task for task in g if task not in taken_tasks.keys() and g.in_degree(task) == 0]
    if available_tasks and len(taken_tasks) < 5:
        for i in range(min([len(available_tasks), (5 - len(taken_tasks))])):
            task = min(available_tasks)
            # A = 65 ascii, Z = 90.  If A takes 60+1 = 61 seconds and Z takes 60+26=86 seconds, ordinal - 4 = time taken
            taken_tasks[task] = ord(task) - 4
            available_tasks.remove(task)
        print("Assigned tasks: {}".format(taken_tasks))
    else:
        min_left = min(taken_tasks.values())
        completed = []
        for task in taken_tasks.keys():
            taken_tasks[task] = taken_tasks[task] - min_left
            if taken_tasks[task] == 0:
                completed.append(task)
                del taken_tasks[task]

        total_time += min_left

        print("completed: {}, tasks left: {}, elapsed time: {}".format(completed, taken_tasks, total_time))
        g.remove_nodes_from(completed)
print(total_time)
