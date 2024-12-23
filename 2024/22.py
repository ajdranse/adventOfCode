from collections import defaultdict


with open('22.in') as f:
    inp = map(int, [x.strip() for x in f.readlines()])

def gen(s):
    r = s * 64
    s = r ^ s
    s = s % 16777216
    r = s // 32
    s = r ^ s
    s = s % 16777216
    r = s * 2048
    s = r ^ s
    s = s % 16777216
    return s

# inp = [1, 2, 3, 2024]
secret = 0
# buy price -> sequence -> list of buyers
# sequence -> buy price -> list of buyers
seq_to_buy_to_buyer_map = defaultdict(lambda: defaultdict(list))
for s in inp:
    start = s
    prev = s % 10
    diff_sequences = defaultdict(list)
    diffs = []
    seen = set()
    for x in range(2000):
        s = gen(s)
        buy = s % 10
        diff = buy - prev
        diffs.append(diff)
        seq = tuple(diffs[-4:])
        if len(diffs) >= 4 and seq not in seen:
            seen.add(seq)
            seq_to_buy_to_buyer_map[seq][buy].append(start)
        prev = buy
    secret += s
print('part1:', secret)

highest_total = 0
highest_seq = None
for seq, m in seq_to_buy_to_buyer_map.items():
    num_buyers = sum([len(b) for b in m.values()])
    total_price = 0
    for buy_price, buyers in m.items():
        total_price += buy_price * len(buyers)
    if total_price > highest_total:
        highest_total = total_price
        highest_seq = seq
        print(f'New {highest_total=} with {seq=}')
print('part2:', highest_seq, highest_total)
