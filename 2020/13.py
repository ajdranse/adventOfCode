import math

earliest = None
raw = []
ids = []
with open('13.in') as f:
# with open('13.test') as f:
    no = 0
    for line in f:
        if no == 0:
            earliest = int(line.rstrip())
        elif no == 1:
            raw = line.rstrip().split(',')
            ids = [int(x) for x in line.rstrip().split(',') if x != 'x']
        no += 1

best_time = 0
best_id = 0
for i in ids:
    next_time = math.ceil(earliest / i) * i
    if best_time == 0 or next_time < best_time:
        best_time = next_time
        best_id = i

print('part1: {}'.format((best_time - earliest) * best_id))

# given input # [7,13,'x','x',59,'x',31,19]
# we get this relation:
# t % 7 == 0
# (t+1) % 13 == 0
# (t+4) % 59 == 0
# (t+6) % 31 == 0
# (t+7) % 19 == 0
#
# which translates to:
# t % 13 == 0
# t % 59 == 55 (59-4)
# t % 31 == 25 (31-6)
# t % 19 == 12 (19-7)
#
# which we can solve using the Chinese Remainder Theorem:
# x = sum[i=i..n](a_i * b_i * invmod(b_i, n_i)) (mod N)
# where N = n_1 * n_2 * ... * n_i
# and b_i = N / n_i
#
# note: we can use the CRT because all of the n-inputs are coprime (in fact, they are all prime)

# using the fact that all of our n-inputs are prime, we know the modular inverse of a mod m is:
# a^(m-2)) % m  (https://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Using_Euler's_theorem)
def invmod(a, m):
    # this does not apply generally
    return (a ** (m-2)) % m

def chinese_remainder(n, a):
    N = 1
    for i in n:
        N *= i

    result = 0
    for n_i, a_i in zip(n, a):
        b_i = N // n_i
        result += a_i * b_i * invmod(b_i, n_i)

    return result % N

n = []
a = []
for idx, i in enumerate(raw):
    if i != 'x':
        n.append(int(i))
        a.append((int(i) - idx) % int(i))
print('part2: {}'.format(chinese_remainder(n, a)))
