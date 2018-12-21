import sys

from sets import Set

def go(part1):
    r1 = 0
    r2 = 0
    r3 = 0
    r4 = 0
    seen = set()
    last = None
    while True:
        r2 = r1 | 0x10000
        r1 = 6663054
        while True:
            r4 = r2 & 0xFF
            r1 = (((r1 + r4) & 0xFFFFFF) * 65899) & 0xFFFFFF
            if 256 > r2:
                if part1:
                # to get minimal instructions, exit first time we get here and print r1
                    return r1
                else:
                    if r1 not in seen:
                        seen.add(r1)
                        last = r1
                        break
                    else:
                        return last

            r2 = r2 // 256


print("part1: {}".format(go(True)))
print("part2: {}".format(go(False)))
