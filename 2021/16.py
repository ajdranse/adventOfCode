from math import prod

with open('16.in') as f:
    lines = f.read().splitlines()

def get_value(type_id, subpackets):
    if type_id == 0: # sum
        return sum([s[3] for s in subpackets])
    elif type_id == 1: # product
        return prod([s[3] for s in subpackets])
    elif type_id == 2: # min
        return min([s[3] for s in subpackets])
    elif type_id == 3: # max
        return max([s[3] for s in subpackets])
    elif type_id == 5: # gt
        return 1 if subpackets[0][3] > subpackets[1][3] else 0
    elif type_id == 6: # lt
        return 1 if subpackets[0][3] < subpackets[1][3] else 0
    elif type_id == 7: # eq
        return 1 if subpackets[0][3] == subpackets[1][3] else 0

def parse_packet(binary):
    version = int(binary[:3], 2)
    type_id = int(binary[3:6], 2)
    if type_id == 4: # literal value
        val = ''
        idx = 6
        stop = False
        while not stop:
            piece = binary[idx:idx+5]
            if piece[0] == '0': # keep reading after this
                stop = True
            val += piece[1:]
            idx += 5
        return ((version, type_id, [], int(val, 2)), idx, binary[idx:])
    else: # operator
        subpackets = []
        length_type_id = int(binary[6])
        if length_type_id == 0:
            bits = int(binary[7:22], 2)
            idx = 22
            remaining = binary[22:]
            read_bits = 0
            while read_bits < bits:
                (subpacket, bits_read, remaining) = parse_packet(remaining)
                subpackets.append(subpacket)
                read_bits += bits_read
            idx += read_bits
        elif length_type_id == 1:
            num = int(binary[7:18], 2)
            idx = 18
            remaining = binary[18:]
            while len(subpackets) < num:
                (subpacket, bits, remaining) = parse_packet(remaining)
                subpackets.append(subpacket)
                idx += bits
        value = get_value(type_id, subpackets)
        return ((version, type_id, subpackets, value), idx, remaining)


def sum_versions(packet):
    s = packet[0]
    if packet[1] != 4:
        s += sum([sum_versions(p) for p in packet[2]])
    return s


for l in lines:
    inp = l

    print(inp)
    binary = ''
    for c in inp:
        binary += str(bin(int(c, base=16)))[2:].zfill(4)

    (packet, idx, remaining) = parse_packet(binary)
    version_sum = sum_versions(packet)
    print(f'part 1: {version_sum}')
    print(f'part 2: {packet[3]}')
