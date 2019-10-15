import copy
import re

class Group:
    def __init__(self, units, hp, atk, atk_type, init, weak, immune_to, group_type, num):
        self.units = int(units)
        self.hp = int(hp)
        self.dead = False
        self.atk = int(atk)
        self.atk_type = atk_type
        self.init = int(init)
        self.weak = weak
        self.immune_to = immune_to
        self.group_type = group_type
        self.target = None
        self.num = num

    def __str__(self):
        if self.dead:
            return "Dead"
        else:
            return "{} {} units, {} hp, {} {} damage (eff power: {}), {} init, weak to {}, immune to {}".format(
                self.group_type,
                self.units,
                self.hp,
                self.atk,
                self.atk_type,
                self.units * self.atk,
                self.init,
                self.weak,
                self.immune_to)

    def acquire(self, avail):
        #   decreasing effective power, choose target
        #   on tie, higher init chooses first
        #   choose target in other group to which it would do most damage
        #       if target is immune to damage type, deals 0
        #       if target is weak to damage type, deals 2x
        #       else 1x
        #   if target tie, choose group with higher power
        #   if still tie, choose group with higher init
        #   if it deals 0 damage to all groups, it chooses no group
        target = None
        dmg_to_target = 0
        for a in avail:
            dmg = self.units * self.atk
            if not a.dead and a.group_type != self.group_type:
                if self.atk_type in a.weak:
                    dmg *= 2
                elif self.atk_type in a.immune_to:
                    dmg = 0

                #print("{} {} would do {} to {} {}".format(self.group_type, self.num, dmg, a.group_type, a.num))

                a_pow = a.units * a.atk
                t_pow = target.units * target.atk if target else -1
                if dmg > 0 and (target is None or dmg > dmg_to_target or (dmg == dmg_to_target and (a_pow > t_pow or a_pow == t_pow and a.init > target.init))):
                    target = a
                    dmg_to_target = dmg

        self.target = target

pattern = re.compile(r'(\d+) units each with (\d+) hit points.*with an attack that does (\d+) ([a-z]+) damage at initiative (\d+)')
weak_pattern = re.compile(r'.*weak to ([a-zA-Z, ]+).*')
immune_pattern = re.compile(r'.*immune to ([a-zA-Z, ]+).*')
immune = []
infection = []
with open('input') as f:
    adding_immune = True
    num = 0
    # 1990 units each with 5438 hit points with an attack that does 25 slashing damage at initiative 20
    for line in f:
        line = line.rstrip()
        if line == 'Immune System:':
            pass
        elif line == 'Infection:':
            adding_immune = False
            num = 0
            continue
        elif line:
            m = re.match(pattern, line)
            c = m.group(1)
            hp = m.group(2)
            atk = m.group(3)
            atk_type = m.group(4)
            init = m.group(5)
            m = re.match(weak_pattern, line)
            weak = []
            if m:
                weak = m.group(1).split(', ')
            m = re.match(immune_pattern, line)
            immune_to = []
            if m:
                immune_to = m.group(1).split(', ')
            num += 1
            if adding_immune:
                immune.append(Group(c, hp, atk, atk_type, init, weak, immune_to, "immune" if adding_immune else "infection", num))
            else:
                infection.append(Group(c, hp, atk, atk_type, init, weak, immune_to, "immune" if adding_immune else "infection", num))

#print("Immune")
#for i in immune:
#    print(i)
#print("Infection")
#for i in infection:
#    print(i)

def go(immune, infection):
    immune_alive = True
    infection_alive = True
    while immune_alive and infection_alive:
        killed_this_round = 0
        #print
        all_groups = sorted(immune + infection, key=lambda x: (x.units * x.atk, x.init), reverse=True)
        available = copy.copy(all_groups)
        for i in all_groups:
            if not i.dead:
                i.acquire(available)
                if i.target:
                    available.remove(i.target)

        all_groups = sorted(all_groups, key=lambda x: x.init, reverse=True)
        for i in all_groups:
            if not i.dead and i.target:
                dmg = i.units * i.atk
                if i.atk_type in i.target.weak:
                    dmg *= 2
                killed = dmg // i.target.hp
                if killed >= i.target.units:
                    killed = i.target.units;
                    i.target.dead = True
                i.target.units -= killed
                killed_this_round += killed
                #print("{} {} (dmg: {}) attacks {} {} (hp: {}) killing {}".format(i.group_type, i.num, dmg, i.target.group_type, i.target.num, i.target.hp, killed))
                i.target = None
        immune_alive = False
        for i in immune:
            if not i.dead:
                immune_alive = True
                #print("{} {} has {} units".format(i.group_type, i.num, i.units))
        infection_alive = False
        for i in infection:
            if not i.dead:
                infection_alive = True
                #print("{} {} has {} units".format(i.group_type, i.num, i.units))
        if killed_this_round == 0:
            return 'stalemate', -1

    left = 0
    for i in immune:
        if not i.dead:
            left += i.units
    for i in infection:
        if not i.dead:
            left += i.units
    return 'immune' if immune_alive else 'infection', left

def boost(immune, infection, boost):
    print("Checking boost {}".format(boost))
    immune_copy = copy.deepcopy(immune)
    for i in immune_copy:
        i.atk += boost
    infection_copy = copy.deepcopy(infection)
    group_alive, left = go(immune_copy, infection_copy)
    print("{} has {} units".format(group_alive, left))
    return group_alive == 'immune'

def binsearch(immune, infection, low = 0, high = None):
    low_bool = boost(immune, infection, low)
    if high is None:
        offset = 1
        while boost(immune, infection, low + offset) == low_bool:
            offset *= 2
        high = low + offset
    else:
        assert boost(immune, infection, high) != low_bool

    best_so_far = low if low_bool else high
    while low <= high:
        mid = (low + high) // 2
        result = boost(immune, infection, mid)
        if result:
            best_so_far = mid
        if result == low_bool:
            low = mid + 1
        else:
            high = mid - 1
    return best_so_far

print("part 1")
boost(immune, infection, 0)
print

boost_num = binsearch(immune, infection)
print
print("part 2")
boost(immune, infection, boost_num)
