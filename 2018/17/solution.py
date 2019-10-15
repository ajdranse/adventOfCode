import re
import sys

from sets import Set

sys.setrecursionlimit(3000)

x_pattern = re.compile(r'.*x=([0-9.]+).*')
y_pattern = re.compile(r'.*y=([0-9.]+).*')

clay = []
with open('input') as f:
    for line in f:
        line = line.rstrip()
        x = re.match(x_pattern, line).group(1)
        y = re.match(y_pattern, line).group(1)
        if '..' in x:
            # range
            xs = x.split('..')
            y = int(y)
            for intx in xrange(int(xs[0]), int(xs[1])+1):
                clay.append((intx, y))
        else:
            x = int(x)
            ys = y.split('..')
            for inty in xrange(int(ys[0]), int(ys[1])+1):
                clay.append((x, inty))

clay = sorted(clay, key=lambda x: (x[1], x[0]))
top = min(clay, key=lambda x: x[1])[1]
bottom = max(clay, key=lambda x: x[1])[1]


def draw(settled, moving, clay):
    xmin = min([i[0] for i in clay])
    xmax = max([i[0] for i in clay])
    for y in xrange(0, clay[-1][1]+2):
        string = ""
        for x in xrange(xmin-1, xmax+1):
            if y == 0 and x == 500:
                string += '+'
            elif (x, y) in clay:
                string += '#'
            elif (x, y) in settled:
                string += '~'
            elif (x, y) in moving:
                string += '|'
            else:
                string += '.'
        print string


settled = Set()
moving = Set()
#draw(settled, moving, clay)


def tick(cur, direction):
    moving.add(cur)
    down = (cur[0], cur[1] + 1)

    if down not in clay and down not in moving and 1 <= down[1] <= bottom:
        # can go down more
        tick(down, "down")

    # down is either clay, already moving, or beyond what we care about

    # can still go down
    if down not in clay and down not in settled:
        return False

    left = (cur[0] - 1, cur[1])
    right = (cur[0] + 1, cur[1])

    # we can probably improve here by not recursing when going left/right
    # recurse left
    left_full = left in clay or left not in moving and tick(left, "left")
    # recurse right
    right_full = right in clay or right not in moving and tick(right, "right")

    # trying to go down but we can't, and we can't go left or right anymore
    if direction == "down" and left_full and right_full:
        settled.add(cur)

        while left in moving:
            settled.add(left)
            left = (left[0] - 1, left[1])

        while right in moving:
            settled.add(right)
            right = (right[0] + 1, right[1])

    # return true if we can't go left anymore
    if direction == "left" and (left_full or left in clay):
        return True
    # return true if we can't go right anymore
    elif direction == "right" and (right_full or right in clay):
        return True
    # error
    else:
        return False


tick((500, 0), "down")

print("Done")
#draw(settled, moving, clay)

accessible = settled | moving
care_about = [a for a in accessible if top <= a[1] <= bottom]
print("part 1: {}".format(len(care_about)))
care_about_settled = [s for s in settled if top <= s[1] <= bottom]
print("part 2: {}".format(len(settled)))
