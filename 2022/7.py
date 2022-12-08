from anytree import NodeMixin, LevelOrderIter


class Directory(NodeMixin):
    def __init__(self, name, parent=None, children=None):
        super(Directory, self).__init__()
        self.name = name
        self.parent = parent
        if children:
            self.children = children

    def get_size(self):
        size = 0
        for c in self.children:
            size += c.get_size()
        return size

    def get_child_names(self):
        return [x.name for x in self.children]

    def get_children(self):
        return self.children

    def get_child(self, name):
        for c in self.children:
            if c.name == name:
                return c
        return None


class File(NodeMixin):
    def __init__(self, name, size, parent=None):
        super(File, self).__init__()
        self.name = name
        self.size = size
        self.parent = parent

    def get_size(self):
        return self.size


lines = []
with open('7.in') as f:
    lines = [x.strip() for x in f.readlines()]

head = Directory('/')
curdir = head
curcmd = None
for line in lines:
    parts = line.split(' ')
    if line.startswith('$'):
        # new command
        if parts[1] == 'cd':
            curcmd = 'cd'
            if parts[2] == '/':
                curdir = head
            elif parts[2] == '..':
                curdir = curdir.parent
            else:
                newdir = curdir.get_child(parts[2])
                if newdir is None:
                    newdir = Directory(parts[2], parent=curdir)
                curdir = newdir
        elif parts[1] == 'ls':
            curcmd = 'ls'
        else:
            raise Exception(f'Error unknown command {parts[1]}')
    elif curcmd == 'ls':
        if line[0].isdigit():
            file = curdir.get_child(parts[1])
            if file is None:
                file = File(parts[1], int(parts[0]), parent=curdir)
        elif line.startswith('dir '):
            pass

total = 0
for node in LevelOrderIter(head):
    if isinstance(node, Directory) and node.get_size() < 100000:
        total += node.get_size()
print(f'part1: {total}')

needed = 30000000 - (70000000 - head.get_size())
candidate = None
for node in LevelOrderIter(head):
    if isinstance(node, Directory) and node.get_size() >= needed:
        if candidate is None or node.get_size() < candidate.get_size():
            candidate = node

print(f'part2: {candidate.get_size()}')
