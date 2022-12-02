loses_to = { 'r': 'p', 'p': 's', 's': 'r' }
beats = { 'r': 's', 'p': 'r', 's': 'p' }
shapes = {'r': 1, 'p': 2, 's': 3}

def map_type(inp):
  if inp == 'A' or inp == 'X':
      return 'r'
  if inp == 'B' or inp == 'Y':
      return 'p'
  if inp == 'C' or inp == 'Z':
      return 's'

def map_type_me(opp, res):
  if res == 'X':
    # lose
    return beats[opp]
  if res == 'Y':
    # draw
    return opp
  if res == 'Z':
    # win
    return loses_to[opp]


def calc(m, o):
  if beats[m] == o:
    return 6
  if loses_to[m] == o:
    return 0
  else:
    return 3


# inp = ['A Y', 'B X', 'C Z']
inp = []
with open('2.in') as f:
  for l in f.readlines():
    inp.append(l.strip())
total = 0
total2 = 0
for l in inp:
    s = l.split(' ')
    opp = map_type(s[0])
    me = map_type(s[1])
    me2 = map_type_me(opp, s[1])
    res = calc(me, opp)
    res2 = calc(me2, opp)
    score = shapes[me] + res
    score2 = shapes[me2] + res2
    total += score
    total2 += score2
print('part 1', total)
print('part 2', total2)
