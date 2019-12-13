import itertools
import re
from sympy import lcm
import numpy as np


def main():
    part_one()
    part_two()


def part_one():
    print("Part One")
    amount = 1000
    with open("input.txt", "r") as input_file:
        moons = []
        for line in input_file:
            x, y, z = re.sub(r"[<>xyz=]", '', line).rstrip().split(",")
            moons.append([int(x), int(y), int(z), 0, 0, 0])
        print(moons)

    for t in range(1, amount + 1):
        for x in range(len(moons)):
            for y in range(x, len(moons)):
                if x == y:
                    continue

                # Apply Gravity

                moons[x][3] += -1 if moons[x][0] > moons[y][0] else (1 if moons[x][0] < moons[y][0] else 0)
                moons[y][3] += 1 if moons[x][0] > moons[y][0] else (-1 if moons[x][0] < moons[y][0] else 0)

                moons[x][4] += -1 if moons[x][1] > moons[y][1] else (1 if moons[x][1] < moons[y][1] else 0)
                moons[y][4] += 1 if moons[x][1] > moons[y][1] else (-1 if moons[x][1] < moons[y][1] else 0)

                moons[x][5] += -1 if moons[x][2] > moons[y][2] else (1 if moons[x][2] < moons[y][2] else 0)
                moons[y][5] += 1 if moons[x][2] > moons[y][2] else (-1 if moons[x][2] < moons[y][2] else 0)

            # Apply velocity
            moons[x][0] += moons[x][3]
            moons[x][1] += moons[x][4]
            moons[x][2] += moons[x][5]
        print(t, total_energy(moons), moons)


def total_energy(moons):
    tot = 0
    for moon in moons:
        pot = abs(moon[0]) + abs(moon[1]) + abs(moon[2])
        kin = abs(moon[3]) + abs(moon[4]) + abs(moon[5])
        tot += pot * kin
    return tot


def part_two():
    print("Part Two")
    with open("input.txt", "r") as input_file:
        moons = []
        for line in input_file:
            x, y, z = re.sub(r"[<>xyz=]", '', line).rstrip().split(",")
            moons.append([int(x), int(y), int(z), 0, 0, 0])
        print(moons)

    first_x = tuple([x[0] for x in moons])
    first_y = tuple([x[1] for x in moons])
    first_z = tuple([x[2] for x in moons])
    i_x = i_y = i_z = 0
    t = 1
    add_x = add_y = add_z = True
    while add_x or add_y or add_z:
        for x in range(len(moons)):
            for y in range(x, len(moons)):
                if x == y:
                    continue

                # Apply Gravity
                moons[x][3] += -1 if moons[x][0] > moons[y][0] else (1 if moons[x][0] < moons[y][0] else 0)
                moons[y][3] += 1 if moons[x][0] > moons[y][0] else (-1 if moons[x][0] < moons[y][0] else 0)

                moons[x][4] += -1 if moons[x][1] > moons[y][1] else (1 if moons[x][1] < moons[y][1] else 0)
                moons[y][4] += 1 if moons[x][1] > moons[y][1] else (-1 if moons[x][1] < moons[y][1] else 0)

                moons[x][5] += -1 if moons[x][2] > moons[y][2] else (1 if moons[x][2] < moons[y][2] else 0)
                moons[y][5] += 1 if moons[x][2] > moons[y][2] else (-1 if moons[x][2] < moons[y][2] else 0)

            # Apply velocity
            moons[x][0] += moons[x][3]
            moons[x][1] += moons[x][4]
            moons[x][2] += moons[x][5]

        t += 1
        if add_x and t != 0 and first_x == tuple(moon[0] for moon in moons):
            i_x = t
            print("X is false!")
            add_x = False

        if add_y and t != 0 and first_y == tuple(moon[1] for moon in moons):
            i_y = t
            print("Y is false!")
            add_y = False

        if add_z and t != 0 and first_z == tuple(moon[2] for moon in moons):
            i_z = t
            print("Z is false!")
            add_z = False
    print(i_x, i_y, i_z, lcm([i_x, i_y, i_z]))


if __name__ == "__main__":
    main()
