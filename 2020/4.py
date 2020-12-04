import re

passports = []
# with open("4.test") as f:
with open("4.in") as f:
    passport = {}
    for line in f:
        if line == "\n" and len(passport) > 0:
            passports.append(passport)
            passport = {}
        else:
            for kv in line.split():
                key, value = kv.split(":")
                passport[key] = value.rstrip()
    passports.append(passport)
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', ] # 'cid']
valid = []
invalid = []
for passport in passports:
    for key in required:
        if key not in passport:
            invalid.append(passport)
            break
    else:
        valid.append(passport)
print(len(passports))
print('part 1: {}'.format(len(valid)))
print('invalid: {}'.format(len(invalid)))

def valid_height(hgt):
    # if height is in cm, between 150 and 193
    if hgt.endswith('cm'):
        hgt = int(hgt[:-2])
        if hgt >= 150 and hgt <= 193:
            return True
    # if height is in inches, between 59 and 76
    elif hgt.endswith('in'):
        hgt = int(hgt[:-2])
        if hgt >= 59 and hgt <= 76:
            return True
    # no other units supported
    return False

valid = []
invalid = []
for p in passports:
    if not(all(k in p for k in required)):
        invalid.append(p)
    else:
        if (int(p['byr']) < 1920 or int(p['byr']) > 2002  # birth year between 1920 and 2002
            or int(p['iyr']) < 2010 or int(p['iyr']) > 2020  # issue year betwen 2010 and 2020
            or int(p['eyr']) < 2020 or int(p['eyr']) > 2030  # expiration year betwen 2020 and 2030
            or not valid_height(p['hgt'])  # height is complicated
            or not re.search(r'^#[0-9a-f]{6}$', p['hcl'])  # hair colour is a valid hex code
            or p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']  # eye colour in given list
            or len(p['pid']) != 9 or not p['pid'].isnumeric()  # passport id is 9 chars long and numeric
        ):
            invalid.append(p)
        else:
            valid.append(p)
print('part 2: {}'.format(len(valid)))
