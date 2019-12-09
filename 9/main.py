import time


def main():
    part_one()
    # part_two()


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
                    numbers[get_index(numbers, relative_base, i + 3, mode_3)] = 1 if int(numbers[get_index(numbers, relative_base, i + 1, mode_1)]) < int(numbers[get_index(numbers, relative_base, i + 2, mode_2)]) else 0
                    increase_amount = 4
                elif n == 8:
                    numbers[get_index(numbers, relative_base, i + 3, mode_3)] = 1 if int(numbers[get_index(numbers, relative_base, i + 1, mode_1)]) == int(numbers[get_index(numbers, relative_base, i + 2, mode_2)]) else 0
                    increase_amount = 4
                elif n == 9:
                    relative_base += numbers[get_index(numbers, relative_base, i + 1, mode_1)]
                    increase_amount = 2
                else:
                    print("Error!")
                    break
                i += increase_amount


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
