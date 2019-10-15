import re
import sys

class Claim:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def __str__(self):
        return "Left: {}, Top: {}, Width: {}, Height: {}".format(self.left, self.top, self.width, self.height)

claims = []
pattern = re.compile(r'.* @ (\d+),(\d+): (\d+)x(\d+)$')
with open('input') as f:
    for line in f:
        m = re.match(pattern, line)
        if len(m.groups()) < 4:
            print("Fail")
            sys.exit(0)
        cur = Claim(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))
        print("{}".format(cur))
        claims.append(cur)

width = 0
height = 0
for claim in claims:
    if claim.left + claim.width > width:
        width = claim.left + claim.width
    if claim.top + claim.height > height:
        height = claim.top + claim.height

array = ['.' for x in range(width * height)]

for claim in claims:
    for y in range(0, claim.height):
        for x in range(0, claim.width):
            index = (x + claim.left) + (width * (y + claim.top))
            #print("Claim {} setting index: ({} + {}) + ({} * ({} + {}) = {}".format(claim, x, claim.left, width, y, claim.top, index))
            if array[index] == '.':
                array[index] = 1
            elif array[index] == 1:
                array[index] = 'X'

#for y in range(0, height):
#    string = ""
#    for x in range(0, width):
#        string += "{} ".format(array[x + y*width])
#    print(string + '.')
#print(' '.join('.' for x in range(0, width+1)))

overlap = 0
for x in array:
    if x == 'X':
        overlap += 1

print(overlap)
