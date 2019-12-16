from collections import defaultdict
from math import floor


def get_inputs(wanted, wanted_amt, surplus, recipes):
    result = []
    if wanted in surplus:
        surplus_amt = surplus[wanted]
        if surplus_amt > wanted_amt:
            surplus[wanted] -= wanted_amt
            return []
        elif surplus_amt == wanted_amt:
            del surplus[wanted]
            return []
        else:
            wanted_amt -= surplus[wanted]
            del surplus[wanted]
    if wanted in recipes:
        wanted_recipe = recipes[wanted]
        if len(wanted_recipe) > 1:
            raise Exception('more than one way to make ', wanted)
        amt_made = list(wanted_recipe.keys())[0]
        ingredients = wanted_recipe[amt_made]
        if amt_made < wanted_amt:
            # need to make multiple times
            result.extend(get_inputs(wanted, wanted_amt - amt_made, surplus, recipes))
            for i in ingredients:
                result.extend(get_inputs(i[0], i[1], surplus, recipes))
        elif amt_made > wanted_amt:
            # need to make once, have surplus
            for i in ingredients:
                result.extend(get_inputs(i[0], i[1], surplus, recipes))
            surplus[wanted] = amt_made - wanted_amt
        else:
            # equals
            for i in ingredients:
                result.extend(get_inputs(i[0], i[1], surplus, recipes))
    else:
        result.append((wanted, wanted_amt))
    return result


def get_root_ingredients(filename):
    recipes = defaultdict(dict)
    ore_recipes = defaultdict(dict)
    print(filename)
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
        for l in lines:
            lhs, rhs = l.split(' => ')
            output = rhs.split(' ')
            inputs = []
            for i in lhs.split(', '):
                split = i.split(' ')
                if split[1] == 'ORE':
                    ore_recipes[output[1]][int(output[0])] = (split[1], int(split[0]))
                else:
                    inputs.append((split[1], int(split[0])))

            if len(inputs) > 0:
                recipes[output[1]][int(output[0])] = inputs

    result = get_inputs('FUEL', 1, {}, recipes)
    ingredients = defaultdict(int)
    for r in result:
        i = r[0]
        amt = r[1]
        ingredients[i] += amt
    # print(ingredients)
    return ingredients, ore_recipes


def make_one_fuel(ingredients, surplus, ore_recipes):
    ore = 0
    for ingredient, amt_needed in ingredients.items():
        if ingredient in surplus:
            surplus_amt = surplus[ingredient]
            if surplus_amt > amt_needed:
                surplus[ingredient] -= amt_needed
                next
            else:
                amt_needed -= surplus[ingredient]
                del surplus[ingredient]

        # print('need {} {}, recipe {}'.format(amt_needed, ingredient, ore_recipes[ingredient]))
        recipe = ore_recipes[ingredient]
        while amt_needed > 0:
            amt_made = list(recipe.keys())[0]
            amt_needed -= amt_made
            ore += recipe[amt_made][1]
        surplus[ingredient] += abs(amt_needed)
    return ore


def run(filename):
    root_ingredients, ore_recipes = get_root_ingredients(filename)
    surplus = defaultdict(int)
    print(make_one_fuel(root_ingredients, surplus, ore_recipes))


def run2(filename, amount_of_ore):
    root_ingredients, ore_recipes = get_root_ingredients(filename)
    surplus = defaultdict(int)
    states = []
    while True:
        ore = make_one_fuel(root_ingredients, surplus, ore_recipes)
        if ((ore, surplus) in states):
            ore_in_cycle = sum(s[0] for s in states)
            fuel_in_cycle = len(states)
            print('seen this state before: ', (ore, surplus))
            print('makes {} fuel, uses {} ore'.format(fuel_in_cycle, ore_in_cycle))
            break
        else:
            states.append((ore, surplus.copy()))
    print(floor(amount_of_ore // ore_in_cycle) * fuel_in_cycle)


run('14.test')
run('14.test.2')
run('14.test.3')
run('14.test.4')
run('14.test.5')
print('part 1: ')
run('14.in')
print('')

run2('14.test.3', 1000000000000)
run2('14.test.4', 1000000000000)
run2('14.test.5', 1000000000000)
print('part 2:')
run2('14.in', 1000000000000)
