import sys
import time
from functools import reduce


def main():
    # part_one()
    part_two()


def part_one():
    print("Part One")
    with open("input.txt", "r") as input_file:
        for line in input_file:
            print("Parsing ", line)
            numbers = list(map(int, line.split(",")))
            numbers = numbers + ([0] * 150)
            print(numbers)
            i = 0
            relative_base = 0
            output = []
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
                    numbers[get_index(numbers, relative_base, i + 1, mode_1)] = input("Int value: ")
                    increase_amount = 2
                elif n == 4:
                    print(numbers[get_index(numbers, relative_base, i + 1, mode_1)])
                    output += [numbers[get_index(numbers, relative_base, i + 1, mode_1)]]
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
            print(output)
            t = (0, 0, 0)
            x = []
            for i in range(len(output)):
                if i % 3 == 0:
                    t = (output[i], t[1], t[2])
                if i % 3 == 1:
                    t = (t[0], output[i], t[2])
                if i % 3 == 2:
                    t = (t[0], t[1], output[i])
                    x += [t]
                    t = (0, 0, 0)
            print(x)
            positions = dict()
            for i in x:
                positions[(i[0], i[1])] = i[2]
            print(positions)
            max_x = reduce(lambda x, y: max(x, y), [i[0] for i in x], 0)
            max_y = reduce(lambda x, y: max(x, y), [i[1] for i in x], 0)
            print("Count: ", [i[2] for i in x].count(2))
            for y in range(max_y + 1):
                for x in range(max_x + 1):
                    sys.stdout.write(str(positions.get(x, y)))
                sys.stdout.write("\n")


def part_two():
    print("Part Two")
    with open("input.txt", "r") as input_file:
        for line in input_file:
            print("Parsing ", line)
            numbers = list(map(int, line.split(",")))
            numbers = numbers + ([0] * 150)
            print(numbers)
            i = 0
            nth_output = 0
            pixel = []
            screen = dict()
            relative_base = 0
            output = []

            ball = (0, 0)
            paddle = (0, 0)
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
                    numbers[get_index(numbers, relative_base, i + 1, mode_1)] = ball[0] - paddle[0]
                    increase_amount = 2
                elif n == 4:
                    nth_output = (nth_output + 1) % 3
                    if nth_output == 0:
                        pixel += [numbers[get_index(numbers, relative_base, i + 1, mode_1)]]
                        screen[(pixel[0], pixel[1])] = pixel[2]
                        if pixel[2] == 4:
                            ball = (pixel[0], pixel[1])
                        if pixel[2] == 3:
                            paddle = (pixel[0], pixel[1])
                        if pixel[0] == -1:
                            print(pixel[2])
                        draw_screen(screen)
                        pixel = []
                    else:
                        pixel += [numbers[get_index(numbers, relative_base, i + 1, mode_1)]]
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
            nth_output += 1


W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple


def draw_screen(positions):
    max_x = reduce(lambda x, y: max(x, y), [i[0] for i in positions.keys()], 0)
    max_y = reduce(lambda x, y: max(x, y), [i[1] for i in positions.keys()], 0)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            n = positions.get((x, y), 0)
            if n == 1:
                sys.stdout.write(B + str(n) + W)
            elif n == 2:
                sys.stdout.write(R + str(n) + W)
            elif n == 3:
                sys.stdout.write(G + str(n) + W)
            elif n == 4:
                sys.stdout.write(O + str(n) + W)
            elif n == 0:
                sys.stdout.write(P + str(n) + W)
        sys.stdout.write("\n")
    print(R + str(positions.get((-1, 0), 0)) + W)


def get_index(numbers, relative_base, i, parameter_mode):
    if int(parameter_mode) == 2:
        return relative_base + numbers[i]
    elif int(parameter_mode) == 1:
        return i
    elif int(parameter_mode) == 0:
        return numbers[i]


if __name__ == "__main__":
    main()
