final = {}
final['b'] = 3176
wires = {}
with open('7.in') as f:
    lines = f.read().splitlines()

signals = {}
for l in lines:
    split = l.split(' -> ')
    wire = split[1]
    signal = split[0].split(' ')
    signals[wire] = signal

interested = 'a'
last_len = 0
while True:
    for wire, signal in signals.items():
        if wire not in final:
            if len(signal) == 1:
                try:
                    val = signal[0]
                    if signal[0] in final:
                        val = final[signal[0]]
                    final[wire] = int(val)
                    # print('Assigned {} to {}'.format(signal[0], wire))
                    signals[wire] = int(signal[0])
                except Exception:
                    pass
            elif len(signal) == 2:
                op = signal[0]
                rhs = signal[1]
                if signal[1] in final:
                    rhs = final[signal[1]]
                try:
                    if op == 'NOT':
                        res = (65536 + ~rhs) % 65536
                        final[wire] = res
                        # print('Assigned ~{} = {} to {}'.format(rhs, res, wire))
                        signals[wire] = [res]
                except Exception:
                    pass
            elif len(signal) == 3:
                lhs = signal[0]
                op = signal[1]
                rhs = signal[2]

                if signal[0] in final:
                    lhs = final[signal[0]]
                if signal[2] in final:
                    rhs = final[signal[2]]
                try:
                    res = None
                    if op == 'RSHIFT':
                        res = int(lhs) >> int(rhs)
                        final[wire] = res
                        # print('Assigned {} >> {} = {} to {}'.format(lhs, rhs, res, wire))
                    elif op == 'LSHIFT':
                        res = int(lhs) << int(rhs)
                        final[wire] = res
                        # print('Assigned {} << {} = {} to {}'.format(lhs, rhs, res, wire))
                    elif op == 'AND':
                        res = int(lhs) & int(rhs)
                        final[wire] = res
                        # print('Assigned {} & {} = {} to {}'.format(lhs, rhs, res, wire))
                    elif op == 'OR':
                        res = int(lhs) | int(rhs)
                        final[wire] = res
                        # print('Assigned {} | {} = {} to {}'.format(lhs, rhs, res, wire))
                    signals[wire] = [res]
                except Exception:
                    pass
            else:
                raise Exception('unknown signal {} for wire {}'.format(signal, wire))

    if interested in final:
        print(final[interested])
        break

    if len(final) == last_len:
        print('not making progress:')
        print(signals)
        print(final)
        break

    last_len = len(final)
