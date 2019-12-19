from functools import reduce

import numpy as np


def main():
    # part_one()
    part_two()


def part_one():
    print("Part One")
    pattern = [0, 1, 0, -1]
    phases = 100
    with open("input.txt", "r") as input_file:
        for line in input_file:
            print(line)
            if len(line.rstrip()) == 0:
                continue
            numbers = np.array([int(x) for x in line])
            for i in range(phases):
                print(i, " / ", phases)
                numbers = calculate(numbers, pattern)
            print(reduce(lambda s, o: str(s) + str(o), numbers[0:8]), "")


def calculate(numbers, pattern):
    result = ""
    for number in range(1, len(numbers) + 1):
        patternToUse = []
        while len(patternToUse) - 1 <= len(numbers):
            patternToUse += [([p] * number) for p in pattern]
        patternToUse = [item for sublist in patternToUse for item in sublist]
        patternToUse = np.array(patternToUse[1:len(numbers) + 1])
        calculated = str(np.inner(patternToUse, numbers))[-1:]

        # print(patternToUse, numbers, calculated)

        result += calculated
    return np.array([int(x) for x in result])


def part_two():
    print("Part Two")
    phases = 100
    with open("input.txt", "r") as input_file:
        for line in input_file:
            print(line)
            if len(line.rstrip()) == 0:
                continue
            numbers = [int(x) for x in line]

            offset = int(''.join(map(str, numbers[:7])))
            numbers = (numbers * 10000)[offset:]
            for _ in range(phases):
                suffix_sum = 0
                for i in range(len(numbers) - 1, -1, -1):
                    numbers[i] = suffix_sum = (suffix_sum + numbers[i]) % 10
            print("n:", ''.join(map(str, numbers[:8])))


if __name__ == "__main__":
    main()
