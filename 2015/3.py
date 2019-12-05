moves = []
with open('3.in') as f:
    moves = [x for x in f.read().splitlines()[0]]

santa_pos = (0, 0)
santa_delivered = {}
santa_delivered[santa_pos] = 1
robosanta_pos = (0, 0)
robosanta_delivered = {}
robosanta_delivered[robosanta_pos] = 1
DX = {'v': 0, '^': 0, '<': -1, '>': 1}
DY = {'v': -1, '^': 1, '<': 0, '>': 0}

for i, m in enumerate(moves):
    if i % 2 == 0:
        santa_pos = (santa_pos[0] + DX[m], santa_pos[1] + DY[m])
        if santa_pos not in santa_delivered:
            santa_delivered[santa_pos] = 1
        else:
            santa_delivered[santa_pos] += 1
    else:
        robosanta_pos = (robosanta_pos[0] + DX[m], robosanta_pos[1] + DY[m])
        if robosanta_pos not in robosanta_delivered:
            robosanta_delivered[robosanta_pos] = 1
        else:
            robosanta_delivered[robosanta_pos] += 1

unique_houses = set(santa_delivered.keys()) | set(robosanta_delivered.keys())
print(len(unique_houses))
