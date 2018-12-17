from collections import deque
from sets import Set


empty_spaces = Set()
pawns = Set()


def printState(round_num, empty_spaces, pawns):
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    for s in empty_spaces:
        if s[0] > end_x:
            end_x = s[0]
        if s[1] > end_y:
            end_y = s[1]
    for p in pawns:
        if p.x > end_x:
            end_x = p.x
        if p.y > end_y:
            end_y = p.y
    print("State after {} rounds".format(round_num))
    for p in pawns:
        if not p.dead:
            print(p)

    for y in xrange(start_y, end_y + 2):
        string = ""
        for x in xrange(start_x, end_x + 2):
            cur = ""
            for p in pawns:
                if not p.dead and x == p.x and y == p.y:
                    cur = p.t
            if not cur:
                if (x, y) not in empty_spaces:
                    cur = "#"
                else:
                    cur = "."
            string += cur
        print(string)


class Pawn:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t
        self.dead = False
        self.hp = 200
        self.atk = 3

    def __str__(self):
        return "({},{}) {} {} {}hp {}atk".format(
            self.x,
            self.y,
            self.t,
            "Alive" if not self.dead else "Dead",
            self.hp,
            self.atk)

    def adjacent(self, other):
        candidates = [(self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]
        if (other.x, other.y) in candidates:
            # print("Adjacent to {}".format(str(other)))
            return True

    def open_squares(self, targets):
        ret = Set()
        for t in targets:
            candidates = [(t.x - 1, t.y), (t.x + 1, t.y), (t.x, t.y - 1), (t.x, t.y + 1)]
            for c in candidates:
                if c in empty_spaces:
                    ret.add(c)
        ret = sorted(ret)
        return ret

    def extract_path(self, path, to):
        ret = []
        cur_space = to
        while cur_space != (self.x, self.y):
            ret.append(cur_space)
            cur_space = path[cur_space]
        return ret

    def get_optimal_move(self, squares):
        paths = []
        for target_square in squares:
            visiting = deque()
            path = {}
            distance = {}
            for visit in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                new_coords = (self.x + visit[0], self.y + visit[1])
                visiting.append(new_coords)
                path[new_coords] = (self.x, self.y)
                distance[new_coords] = 1

            while len(visiting) > 0:
                cur_space = visiting.popleft()
                if cur_space[0] == target_square[0] and cur_space[1] == target_square[1]:
                    cur_path = list(reversed(self.extract_path(path, cur_space)))
                    cur_distance = distance[cur_space]
                    # first step, distance, target square, full path
                    paths.append((cur_path[0], cur_distance, target_square, cur_path))

                    ## print("Found target square: {} at distance {}".format(target_square, distance[cur_space]))
                    #if distance[cur_space] < optimal_distance:
                    #    optimal_distance = distance[cur_space]
                    #    optimal_path = list(reversed(self.extract_path(path, cur_space)))
                    #    # print("New optimal with path: {}".format(list(reversed(self.extract_path(path, cur_space)))))
                    #elif distance[cur_space] == optimal_distance:
                    #    # print("Tied for distance with path: {}".format(cur_path))
                    #    if (cur_path[-1][1] < optimal_path[-1][1]) or (cur_path[-1][1] == optimal_path[-1][1] and cur_path[0][0] < optimal_path[-1][0]):
                    #        # print("New optimal path based on lower reading order")
                    #        optimal_path = cur_path
                    continue
                if cur_space not in empty_spaces:
                    continue
                occupied = False
                for p in pawns:
                    if not p.dead and cur_space[0] == p.x and cur_space[1] == p.y:
                        # print("Space {} occupied by pawn {}".format(cur_space, p))
                        occupied = True
                if occupied:
                    continue

                for visit in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    new_coords = (cur_space[0] + visit[0], cur_space[1] + visit[1])
                    if new_coords not in path:
                        path[new_coords] = cur_space
                        distance[new_coords] = distance[cur_space] + 1
                        visiting.append(new_coords)

        if len(paths) == 0:
            return (None, None)

        # choose shortest path
        min_distance = min([p[1] for p in paths])
        paths = [p for p in paths if p[1] == min_distance]

        # if tie, choose first end space in reading order
        paths.sort(key=lambda x: (x[2][1], x[2][0]))
        paths = [p for p in paths if p[2] == paths[0][2]]

        # if tie, take first step in reading order
        paths.sort(key=lambda x: (x[0][1], x[0][0]))
        paths = [p for p in paths if p[0] == paths[0][0]]

        return paths[0][0]
        #if optimal_path:
        #    return (optimal_path[0][0], optimal_path[0][1])
        #else:
        #    return (None, None)

    def move(self):
        # print("{} moving".format(self))
        # identify targets
        targets = [p for p in pawns if p.t != self.t and not p.dead]
        if len(targets) == 0:
            # print("No targets, combat is done!")
            return False
        targets = sorted(targets, key=lambda x: (x.x, x.y, x.hp))
        # print("My targets: {}".format([str(p) for p in targets]))
        # check if next to any target
        for t in targets:
            if self.adjacent(t):
                # if true don't move
                return True
        # identify open squares next to targets
        open_squares = self.open_squares(targets)
        # find closest path to available squares
        # if paths are tied, choose first in reading order
        (next_x, next_y) = self.get_optimal_move(open_squares)
        if next_x and next_y:
            # take a single step
            # print("{} moving to ({},{})".format(self, next_x, next_y))
            empty_spaces.add((self.x, self.y))
            empty_spaces.remove((next_x, next_y))
            self.x = next_x
            self.y = next_y
        return True

    def attack(self):
        # find all adjacent targets
        targets = [p for p in pawns if p.t != self.t and not p.dead and (abs(self.x - p.x) + abs(self.y - p.y)) == 1]
        targets = sorted(targets, key=lambda x: (x.hp, x.y, x.x))
        # choose target with fewest hp
        if len(targets) > 0:
            # if tied, choose first in reading order
            target = targets[0]
            # print("Chose target: {}".format(str(target)))
            # deal attack power damage to target
            target.hp -= self.atk
            # if target hp <= 0, target dies
            if target.hp <= 0:
                target.dead = True
                empty_spaces.add((target.x, target.y))

lines = []
with open('test6') as f:
    for line in f:
        line = line.rstrip()
        lines.append(line)

for line in lines:
    print(line)

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == '.':
            empty_spaces.add((x, y))
        elif c in 'EG':
            pawns.add(Pawn(x, y, c))

pawns = sorted(pawns, key=lambda x: (x.y, x.x))
round_num = 0
combat = True
while combat:
    round_num += 1
    for p in pawns:
        if p.dead:
            continue
        if not p.move():
            combat = False
            break
        p.attack()
    pawns = sorted(pawns, key=lambda x: (x.y, x.x))
    printState(round_num, empty_spaces, pawns)

full_rounds = round_num - 1
print("Combat took: {} full rounds".format(full_rounds))
hp = sum([p.hp for p in pawns if not p.dead])
print("HP of alive pawns: {}".format(hp))
print("outcome: {}".format(full_rounds * hp))
