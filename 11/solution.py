def get_power_level(x, y, serial_no):
    intermediate = ((((x+10) * y) + serial_no) * (x+10))
    return ((intermediate // 100) % 10) - 5

power_levels = {}
for x in xrange(300):
    for y in xrange(300):
        power_levels[(x, y)] = get_power_level(x, y, 7315)

def block_power(start_x, start_y, grid_size):
    ret = 0
    for y in xrange(start_y, start_y+grid_size):
        if y > 299:
            return None
        for x in xrange(start_x, start_x+grid_size):
            if x > 299:
                return None
            cur_power = power_levels[(x, y)]
            ret += cur_power
    return ret

print("Part 1")
start_x = 0
start_y = 0
max_power = 0
for x in xrange(300):
    for y in xrange(300):
        power = block_power(x, y, 3)
        if power > max_power:
            start_x = x
            start_y = y
            max_power = power
print("Max block has top-left {}, {}, power: {}".format(start_x, start_y, max_power))

print("Part 2")
start_x = 0
start_y = 0
max_power = 0
grid_size = 0
for i in xrange(1, 300):
    print("Checking grid size {}".format(i))
    for x in xrange(300):
        for y in xrange(300):
            power = block_power(x, y, i)
            if power > max_power:
                start_x = x
                start_y = y
                max_power = power
                grid_size = i
                print("New max block grid size {} with top-left {}, {} has power: {}".format(grid_size, start_x, start_y, max_power))
print("Max block has top-left {}, {}, grid size {}, power: {}".format(start_x, start_y, grid_size, max_power))
