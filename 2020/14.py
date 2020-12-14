import re
from collections import defaultdict, deque
def run(filename, pt2):
    mask = None
    memory = defaultdict(int)
    with open(filename) as f:
        for line in f:
            if line.startswith('mask = '):
                mask = re.search('mask = (.*)', line).group(1)
            elif line.startswith('mem'):
                m = re.search('mem\[(\d+)\] = (\d+)', line)
                addr = '{0:b}'.format(int(m.group(1)))
                addr = addr.rjust(36, '0')
                val = '{0:b}'.format(int(m.group(2)))
                val = val.rjust(36, '0')
                for idx, i in enumerate(mask):
                    if pt2:
                        if i == '1':
                            addr = addr[:idx] + '1' + addr[idx+1:]
                        elif i == 'X':
                            addr = addr[:idx] + 'X' + addr[idx+1:]
                    else:
                        if i != 'X':
                            if i == '1':
                                val = val[:idx] + '1' + val[idx+1:]
                            elif i == '0':
                                val = val[:idx] + '0' + val[idx+1:]
                if pt2:
                    addrs = []
                    q = deque()
                    q.append(addr)
                    while q:
                        a = q.pop()
                        if 'X' in a:
                            idx = a.find('X')
                            q.append(a[:idx] + '0' + a[idx+1:])
                            q.append(a[:idx] + '1' + a[idx+1:])
                        else:
                            addrs.append(a)
                    for a in addrs:
                        memory[int(a, 2)] = int(val, 2)
                else:
                    memory[int(addr, 2)] = int(val, 2)
    return memory.values()

print('part1: {}'.format(sum(run('14.in', False))))
print('part2: {}'.format(sum(run('14.in', True))))
