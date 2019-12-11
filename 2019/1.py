lines = []
with open('1.in') as f:
    lines = f.read().splitlines()

print('part 1')
sum = 0
for mass in lines:
    fuel = int(int(mass) / 3) - 2
    sum += fuel
print(sum)

print('part 2')
sum = 0
for mass in lines:
    fuel = int(int(mass) / 3) - 2
    while fuel > 0:
        sum += fuel
        fuel = int(fuel / 3) - 2
print(sum)
