from collections import deque, defaultdict

def play(num_players, last_marble_value):
    player_scores = defaultdict(int)
    circle = deque([0])
    for marble in range(1, last_marble_value+1):
        if marble % 23 == 0:
            circle.rotate(7)
            player_scores[marble % num_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(player_scores.values())


if __name__ == "__main__":
    print(play(435, 7118400))
