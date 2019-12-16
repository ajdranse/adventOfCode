import numpy as np

base_pattern = [0, 1, 0, -1]

test1 = '12345678'
test2 = '80871224585914546619083218645595'
test3 = '19617804207202209144916044189917'
test4 = '69317163492948606335995924319873'


def fft(inp):
    final_output = ''
    for i in range(100):
        if i % 10 == 0:
            print(i)
        output = ''
        for idx in range(len(inp)):
            pattern = [item for sublist in [np.repeat(p, idx+1) for p in base_pattern] for item in sublist]
            pattern_idx = 1
            out = 0
            for c_idx, c in enumerate(inp):
                c = int(c)
                mult = pattern[pattern_idx]
                pattern_idx = (pattern_idx + 1) % len(pattern)
                out += (c * mult)
            out = abs(out) % 10
            output += str(out)
        inp = output
        final_output = output
        output = ''
    print(final_output)


# fft(test2)
# fft(test3)
# fft(test4)
with open('16.in') as f:
    inp = f.readline().strip()
    print('part1')
    fft(inp)

with open('16.in') as f:
    input_string = f.read().strip()

    # get offset to read
    offset = int(input_string[:7])
    # repeat list
    part2 = list(map(int, input_string)) * 10000
    # do fft 100 times
    for i in range(100):
        # get sum of everything after offset
        sum_of_all_after_offset = sum(part2[j] for j in range(offset, len(part2)))
        # for each position in the output that we care about
        for j in range(offset, len(part2)):
            # copy current partial sum
            partial = sum_of_all_after_offset
            # remove the value of current character from sum
            sum_of_all_after_offset -= part2[j]
            # write output sum
            part2[j] = abs(partial) % 10
    print(part2[offset:offset+8])
