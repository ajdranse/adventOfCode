def parse(filename):
    lines = []
    with open(filename) as f:
        lines = f.read().splitlines()

    numbers = [int(x) for x in lines[0].split(',')]

    boards = []
    idx = 2
    while idx < len(lines):
        board = []
        for line in lines[idx:idx+5]:
            row = []
            for x in line.split():
                row.append(int(x))
            board.append(row)
        boards.append(board)
        idx += 6
    return (numbers, boards)

def go(numbers, boards):
    won = []
    for n in numbers:
        for b in boards:
            for y in range(5):
                for x in range(5):
                    if b[y][x] == n:
                        b[y][x] = 'x'

        for b in boards:
            for y in range(5):
                if set(b[y]) == set('x'):
                    won.append((b, n))
                    boards.remove(b)
                    break

        for b in boards:
            for x in range(5):
                if set([b[y][x] for y in range(5)]) == set('x'):
                    won.append((b, n))
                    boards.remove(b)
                    break
        if len(boards) == 0:
            break

    return won

def main():
    (numbers, boards) = parse('4.in')
    winners = go(numbers, boards)

    (winner_1, num_1) = winners[0]
    s = sum([item if item != 'x' else 0 for sublist in winner_1 for item in sublist])
    print(f'part 1: {s * num_1}')

    (winner_2, num_2) = winners[-1]
    s = sum([item if item != 'x' else 0 for sublist in winner_2 for item in sublist])
    print(f'part 2: {s * num_2}')

if __name__ == '__main__':
    main()
