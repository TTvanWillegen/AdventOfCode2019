import time
from functools import reduce


def main():
    part_one()
    # part_two()


def part_one():
    print("Part One")
    with open("input.txt", "r") as input_file:
        for line in input_file:
            print("Parsing ", line)
            if len(line.rstrip()) == 0:
                continue
            numbers = list(map(int, line.split(",")))
            numbers = numbers + ([0] * 5000)
            print(numbers)
            i = 0
            relative_base = 0
            x = 0
            y = 0
            world = {}
            j = 0

            # L,10,L,6,R,10,R,6,R,8,R,8,L,6,R,8,L,10,L,6,R,10,L,10,R,8,R,8,L,10,R,6,R,8,R,8,L,6,R,8,L,10,R,8,R,8,L,10,R,6,R,8,R,8,L,6,R,8,L,10,L,6,R,10,L,10,R,8,R,8,L,10,R,6,R,8,R,8,L,6,R,8
            #
            # Main - 65 44 66 44 65 44 67 44 66 44 67 44 66 44 65 44 67 44 66	10
            #
            # A - 76 44 49 48 44 76 44 54 44 82 44 49 48						10
            # B - 82 44 54 44 82 44 56 44 82 44 56 44 76 44 54 44 82 44 56	10
            # C - 76 44 49 48 44 82 44 56 44 82 44 56 44 76 44 49 48			10
            #
            # 110 10

            input_numbers = [65, 44, 66, 44, 65, 44, 67, 44, 66, 44, 67, 44, 66, 44, 65, 44, 67, 44, 66, 10, 76, 44, 49, 48, 44, 76, 44, 54, 44, 82, 44, 49, 48, 10, 82, 44, 54, 44, 82, 44, 56, 44, 82,
                             44, 56, 44, 76, 44, 54, 44, 82, 44, 56, 10, 76, 44, 49, 48, 44, 82, 44, 56, 44, 82, 44, 56, 44, 76, 44, 49, 48, 10, 110, 10]
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
                    numbers[get_index(numbers, relative_base, i + 1, mode_1)] = input_numbers[j]
                    j += 1
                    increase_amount = 2
                elif n == 4:
                    nr = numbers[get_index(numbers, relative_base, i + 1, mode_1)]
                    if nr > 200:
                        print("Number:", nr)
                        break
                    char = chr(nr)
                    print(char, end="")
                    world[(x, y)] = char

                    if nr == 10:
                        y += 1
                        x = 0
                    else:
                        x += 1

                    if char == "X":
                        print("OH NOES YOU HAVE LOST CONTROL OF YOUR VACUUM!")
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
            intersections = list(filter(
                lambda location:
                world.get((location[0], location[1]), ".") == "#" and
                world.get((location[0], location[1] - 1), ".") == "#" and
                world.get((location[0], location[1] + 1), ".") == "#" and
                world.get((location[0] - 1, location[1]), ".") == "#" and
                world.get((location[0] + 1, location[1]), ".") == "#"
                , world))
            print(intersections)
            alignment = reduce(lambda i, o: i + (o[0] * o[1]), intersections, 0)
            print(alignment)


def part_two():
    print("Part Two")


def get_index(numbers, relative_base, i, parameter_mode):
    if int(parameter_mode) == 2:
        return relative_base + numbers[i]
    elif int(parameter_mode) == 1:
        return i
    elif int(parameter_mode) == 0:
        return numbers[i]


if __name__ == "__main__":
    main()
