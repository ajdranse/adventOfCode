import numpy as np
import re


def load(filename):
    moons_pos = []
    moons_vel = []
    with open(filename) as f:
        for x in f.readlines():
            m = re.match(r'<x=(.*), y=(.*), z=(.*)>', x)
            if m:
                moons_pos.append([int(m.group(1)), int(m.group(2)), int(m.group(3))])
                moons_vel.append([0, 0, 0])
    return moons_pos, moons_vel


def update(pos, vel):
    for m_idx, m in enumerate(pos):
        for m2_idx in range(len(m)+1):
            if m_idx != m2_idx:
                m2 = pos[m2_idx]
                for j in range(3):
                    if m[j] > m2[j]:
                        vel[m_idx][j] -= 1
                    elif m[j] < m2[j]:
                        vel[m_idx][j] += 1

    for idx in range(len(pos)):
        for j in range(3):
            pos[idx][j] += vel[idx][j]


def calc(positions):
    velocities = [0] * len(positions)
    first = tuple(positions) + tuple(velocities)
    steps = 0
    while True:
        for idx in range(len(positions)):
            for idx2 in range(len(positions)):
                if idx != idx2:
                    if positions[idx] > positions[idx2]:
                        velocities[idx] -= 1
                    elif positions[idx] < positions[idx2]:
                        velocities[idx] += 1
        for idx in range(len(positions)):
            positions[idx] += velocities[idx]

        steps += 1
        if first == (tuple(positions) + tuple(velocities)):
            return steps


def run(filename):
    print(filename)
    moons_pos, moons_vel = load(filename)
    steps = 0
    while steps < 1000:
        update(moons_pos, moons_vel)
        steps += 1
    total = 0
    for idx, m in enumerate(moons_pos):
        pot = abs(m[0]) + abs(m[1]) + abs(m[2])
        kin = abs(moons_vel[idx][0]) + abs(moons_vel[idx][1]) + abs(moons_vel[idx][2])
        total += pot * kin
    print('part1:', total)

    moons_pos, _ = load(filename)
    x_period = calc([m[0] for m in moons_pos])
    y_period = calc([m[1] for m in moons_pos])
    z_period = calc([m[2] for m in moons_pos])
    lcm = np.lcm.reduce([x_period, y_period, z_period])
    print('part2:', x_period, y_period, z_period, lcm)


run('12.test')
run('12.test.2')
run('12.in')
