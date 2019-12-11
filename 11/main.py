import sys
import time
from functools import reduce


def main():
    part_one()
    part_two()


def part_one():
    print("Part One")
    with open("input.txt", "r") as input_file:
        for line in input_file:
            print("Parsing ", line)
            numbers = list(map(int, line.split(",")))
            numbers = numbers + ([0] * 1000)
            colored = intcode(numbers, current=(0, 0), color=dict())
            print(len(colored), colored)


def part_two():
    print("Part Two")
    with open("input.txt", "r") as input_file:
        for line in input_file:
            print("Parsing ", line)
            numbers = list(map(int, line.split(",")))
            numbers = numbers + ([0] * 1000)
            cdict = dict()
            cdict[(0,0)] = 1
            colored = intcode(numbers, current=(0, 0), color=cdict)
            print(len(colored), colored)
            max_x = reduce(lambda x, y: max(x, y[0]), colored, 0)
            max_y = reduce(lambda x, y: max(x, y[1]), colored, 0)
            min_x = reduce(lambda x, y: min(x, y[0]), colored, 0)
            min_y = reduce(lambda x, y: min(x, y[1]), colored, 0)
            for y in range(min_y, max_y+1):
                for x in range(min_y, max_x + 1):
                    color = colored.get((x, y), 0)
                    if color == 0:
                        sys.stdout.write('░')
                    if color == 1:
                        sys.stdout.write('█')
                sys.stdout.write('\n')


def get_index(numbers, relative_base, i, parameter_mode):
    if int(parameter_mode) == 2:
        return relative_base + numbers[i]
    elif int(parameter_mode) == 1:
        return i
    elif int(parameter_mode) == 0:
        return numbers[i]


def get_new(current, facing, turning_left):
    if facing == "^":
        if turning_left:
            current = (current[0] - 1, current[1])
            facing = "<"
        else:
            current = (current[0] + 1, current[1])
            facing = ">"
    elif facing == "<":
        if turning_left:
            current = (current[0], current[1] + 1)
            facing = "v"
        else:
            current = (current[0], current[1] - 1)
            facing = "^"
    elif facing == "v":
        if turning_left:
            current = (current[0] + 1, current[1])
            facing = ">"
        else:
            current = (current[0] - 1, current[1])
            facing = "<"
    elif facing == ">":
        if turning_left:
            current = (current[0], current[1] - 1)
            facing = "^"
        else:
            current = (current[0], current[1] + 1)
            facing = "v"
    return current, facing


def intcode(numbers, current, color, i=0, relative_base=0):
    print(numbers)
    painted = set()
    first_output = True
    facing = "^"
    while i < len(numbers):
        (mode_3, mode_2, mode_1, opcode_1, opcode_2) = str(numbers[i]).zfill(5)
        n = int((opcode_1 if opcode_1 != "0" else "") + opcode_2)
        if n == 99:
            break
        if n == 1:
            n1 = numbers[get_index(numbers, relative_base, i + 1, mode_1)]
            n2 = numbers[get_index(numbers, relative_base, i + 2, mode_2)]
            numbers[get_index(numbers, relative_base, i + 3, mode_3)] = int(n1) + int(n2)
            increase_amount = 4
        elif n == 2:
            n1 = numbers[get_index(numbers, relative_base, i + 1, mode_1)]
            n2 = numbers[get_index(numbers, relative_base, i + 2, mode_2)]
            numbers[get_index(numbers, relative_base, i + 3, mode_3)] = n1 * n2
            increase_amount = 4
        elif n == 3:
            numbers[get_index(numbers, relative_base, i + 1, mode_1)] = color.get(current, 0)
            increase_amount = 2
        elif n == 4:
            print(current, numbers[get_index(numbers, relative_base, i + 1, mode_1)])
            if first_output:
                color[current] = numbers[get_index(numbers, relative_base, i + 1, mode_1)]
                painted.add(current)
                first_output = False
            else:
                turning_left = numbers[get_index(numbers, relative_base, i + 1, mode_1)] == 0
                current, facing = get_new(current, facing, turning_left)
                first_output = True
            increase_amount = 2
        elif n == 5:
            condition_value = numbers[get_index(numbers, relative_base, i + 1, mode_1)]
            if int(condition_value) != 0:
                i = numbers[get_index(numbers, relative_base, i + 2, mode_2)]
                increase_amount = 0
            else:
                increase_amount = 3
        elif n == 6:
            condition_value = numbers[get_index(numbers, relative_base, i + 1, mode_1)]
            if int(condition_value) == 0:
                i = numbers[get_index(numbers, relative_base, i + 2, mode_2)]
                increase_amount = 0
            else:
                increase_amount = 3
        elif n == 7:
            numbers[get_index(numbers, relative_base, i + 3, mode_3)] = 1 if int(numbers[get_index(numbers, relative_base, i + 1, mode_1)]) < int(
                numbers[get_index(numbers, relative_base, i + 2, mode_2)]) else 0
            increase_amount = 4
        elif n == 8:
            numbers[get_index(numbers, relative_base, i + 3, mode_3)] = 1 if int(numbers[get_index(numbers, relative_base, i + 1, mode_1)]) == int(
                numbers[get_index(numbers, relative_base, i + 2, mode_2)]) else 0
            increase_amount = 4
        elif n == 9:
            relative_base += numbers[get_index(numbers, relative_base, i + 1, mode_1)]
            increase_amount = 2
        else:
            print("Error!")
            break
        i += increase_amount
    return color


if __name__ == "__main__":
    main()
