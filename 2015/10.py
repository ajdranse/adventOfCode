inp = '1113122113'
test = '1'


def do(string):
    out = ''
    amt = 0
    i = 0
    while i < len(string):
        c = string[i]
        amt = 1
        while i+1 < len(string) and string[i+1] == c:
            amt += 1
            i += 1
        out += str(amt) + c
        i += 1
    return out


def run(input_string):
    print(input_string)
    for i in range(40):
        input_string = do(input_string)
    print(len(input_string))


def run2(input_string):
    print(input_string)
    for i in range(50):
        input_string = do(input_string)
    print(len(input_string))


run(test)
print('part1')
run(inp)
print('part2')
run2(inp)
