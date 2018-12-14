def iterate(scores, first_idx, second_idx):
    first = scores[first_idx]
    second = scores[second_idx]
    summed = first + second
    digits = [int(d) for d in str(summed)]
    scores += digits
    first_idx = (first_idx + 1 + first) % len(scores)
    second_idx = (second_idx + 1 + second) % len(scores)
    return(scores, first_idx, second_idx)

def iterate_2(scores, first_idx, second_idx):
    (scores, first_idx, second_idx) = iterate(scores, first_idx, second_idx)
    last = scores[-6:]
    last2 = scores[-6-1:-1]
    return (last, last2, scores, first_idx, second_idx)

scores = [3, 7]
first_idx = 0
second_idx = 1

while len(scores) < 190240:
    (scores, first_idx, second_idx) = iterate(scores, first_idx, second_idx)

start_idx = 190221
print("part1: {}".format(scores[start_idx:10+start_idx]))

scores = [3, 7]
first_idx = 0
second_idx = 1
last = []
last2 = []
wanted = [1,9,0,2,2,1]
while last != wanted and last2 != wanted:
    (last, last2, scores, first_idx, second_idx) = iterate_2(scores, first_idx, second_idx)
if last == wanted:
    print(len(scores) - len(wanted))
elif last2 == wanted:
    print(len(scores) - len(wanted) - 1)
