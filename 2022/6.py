def do(inp):
    s = 0
    e = 4
    while e < len(inp):
        if len(set(inp[s:e])) == 4:
            print(e)
            break
        s += 1
        e += 1


def do2(inp):
    s = 0
    e = 14
    while e < len(inp):
        if len(set(inp[s:e])) == 14:
            print(e)
            break
        s += 1
        e += 1


print('part1')
do('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
do('bvwbjplbgvbhsrlpgdmjqwftvncz')
do('nppdvjthqldpwncqszvftbrmjlhg')
do('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
do('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
with open('6.in') as f:
    inp = f.readlines()[0].strip()
    do(inp)

print('part2')
do2('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
do2('bvwbjplbgvbhsrlpgdmjqwftvncz')
do2('nppdvjthqldpwncqszvftbrmjlhg')
do2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
do2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
with open('6.in') as f:
    inp = f.readlines()[0].strip()
    do2(inp)
