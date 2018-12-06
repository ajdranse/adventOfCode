from collections import defaultdict

array = []

def closest_neighbour(x, y):
    closest = None
    min_distance = None
    count = 0
    for loc in array:
        distance = abs(loc[0] - x) + abs(loc[1] - y)
        # tied, no closest
        if distance == min_distance:
            count += 1
        if min_distance is None or distance < min_distance:
            count = 1
            closest = loc
            min_distance = distance

    if count > 1:
        return (-1e6, -1e6)
    return closest

def get_scores(min_x, max_x, min_y, max_y):
    scores = defaultdict(int)
    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            scores[closest_neighbour(i, j)] += 1
    return scores

if __name__ == "__main__":
    with open('input') as f:
        for line in f:
            line = line.rstrip()
            tup = tuple(int(x) for x in line.split(','))
            array.append(tup)

    total_width = max(zip(*array)[0])
    total_height = max(zip(*array)[1])

    min_x = 0
    max_x = total_width
    min_y = 0
    max_y = total_height

    scores = get_scores(min_x, max_x, min_y, max_y)

    min_x = -total_width
    max_x = total_width*2
    min_y = -total_height
    max_y = total_height*2

    scores2 = get_scores(min_x, max_x, min_y, max_y)

    bounded = []
    for loc, score in scores.iteritems():
        if scores2[loc] == score:
            bounded.append((score, loc))

    bounded.sort()
    for b in bounded:
        print(b)
