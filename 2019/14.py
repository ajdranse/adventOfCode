from collections import defaultdict


def get_fuel(wanted_amt, recipes):
    needed = {'FUEL': wanted_amt}
    surplus = defaultdict(int)
    while True:
        try:
            # print('needed: ', needed)
            # print('surplus: ', surplus)
            making = next(n for n in needed if n != 'ORE')
            # print('making {}'.format(making))
        except StopIteration:
            break
        amt_made, inputs = recipes[making]
        # print('make {} from {}'.format(amt_made, inputs))
        times, remainder = divmod(needed[making], amt_made)
        if remainder == 0:
            # exact
            del needed[making]
        else:
            del needed[making]
            surplus[making] = amt_made - remainder
            times += 1  # to account for remainder

        # print('need to make {} times'.format(times))

        for amt, ingredient in inputs:
            # already needed + amount for this - surplus
            already = needed.get(ingredient, 0)
            forthis = amt * times
            surplus_amt = surplus[ingredient]
            if already + forthis - surplus_amt > 0:
                needed[ingredient] = already + forthis - surplus_amt
                del surplus[ingredient]
            else:
                surplus[ingredient] -= already + forthis
            # print('need {} of {}'.format(needed.get(ingredient, 0), ingredient))
    return needed['ORE']


def get_recipes(filename):
    recipes = defaultdict(dict)
    print(filename)
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        for l in lines:
            lhs, rhs = l.split(' => ')
            output = rhs.split(' ')
            inputs = []
            for i in lhs.split(', '):
                split = i.split(' ')
                inputs.append((int(split[0]), split[1]))

            recipes[output[1]] = (int(output[0]), inputs)
    return recipes


def run(filename):
    recipes = get_recipes(filename)
    print(get_fuel(1, recipes))


def run2(filename, target):
    recipes = get_recipes(filename)
    lo = 0
    hi = 1
    ore = 0
    while ore < target:
        lo, hi = hi, hi*10
        ore = get_fuel(hi, recipes)

    while hi-lo > 1:
        mid = (lo + hi) // 2
        ore = get_fuel(mid, recipes)
        if ore > target:
            hi = mid
        else:
            lo = mid
    return mid


run('14.test')
run('14.test.2')
run('14.test.3')
run('14.test.4')
run('14.test.5')
print('part 1: ')
run('14.in')
print('')

print(run2('14.test.3', 1e12))
print(run2('14.test.4', 1e12))
print(run2('14.test.5', 1e12))
part2 = run2('14.in', 1e12)
for i in range(part2-2, part2+3):
    ore = get_fuel(i, get_recipes('14.in'))
    print(i, ore)
# print('part 2: ', part2)
