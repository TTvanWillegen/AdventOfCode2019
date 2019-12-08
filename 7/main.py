import itertools


def main():
    # part_one()
    part_two()


def part_one():
    print("Part One")
    with open("input.txt", "r") as input_file:
        codes = [x for x in range(5, 10)]
        coding_permutations = list(itertools.permutations(codes))
        result = 0
        for line in input_file:
            print("Parsing ", line)
            for permutation in coding_permutations:
                states = [0 for x in range(0, 5)]
                numbers = list(map(int, line.split(",")))
                j = 0
                while states[4] is not None:
                    (r1, states[0]) = int_code(numbers, [permutation[0], 0], states[0], j)
                    (r2, states[1]) = int_code(numbers, [permutation[1], r1], states[1], j)
                    (r3, states[2]) = int_code(numbers, [permutation[2], r2], states[2], j)
                    (r4, states[3]) = int_code(numbers, [permutation[3], r3], states[3], j)
                    (r5, states[4]) = int_code(numbers, [permutation[4], r4], states[4], j)
                    j = 1
                result = max(result, r5)
        print(result)


def part_two():
    print("Part Two")
    with open("input.txt", "r") as input_file:
        codes = [x for x in range(5, 10)]
        coding_permutations = list(itertools.permutations(codes))
        result = 0
        for line in input_file:
            print("Parsing ", line)
            for permutation in coding_permutations:
                states = [0 for x in range(0, 5)]
                results = [0 for x in range(0, 5)]
                numbers = list(map(int, line.split(",")))
                j = 0
                while states[4] is not None:
                    (results[0], states[0]) = int_code(numbers, [permutation[0], results[4]], states[0], j, results[0])
                    (results[1], states[1]) = int_code(numbers, [permutation[1], results[0]], states[1], j, results[1])
                    (results[2], states[2]) = int_code(numbers, [permutation[2], results[1]], states[2], j, results[2])
                    (results[3], states[3]) = int_code(numbers, [permutation[3], results[2]], states[3], j, results[3])
                    (results[4], states[4]) = int_code(numbers, [permutation[4], results[3]], states[4], j, results[4])
                    j = 1
                result = max(int(result), int(results[4]))
        print(result)


def int_code(numbers, input, i=0, j=0, result = 0):
    while i < len(numbers):
        (mode_3, mode_2, mode_1, opcode_1, opcode_2) = str(numbers[i]).zfill(5)
        n = int((opcode_1 if opcode_1 != "0" else "") + opcode_2)
        if n == 99:
            return result, None
        if n == 1:
            n1 = numbers[get_index(numbers, i + 1, mode_1)]
            n2 = numbers[get_index(numbers, i + 2, mode_2)]
            numbers[get_index(numbers, i + 3, mode_3)] = int(n1) + int(n2)
            increase_amount = 4
        elif n == 2:
            n1 = numbers[get_index(numbers, i + 1, mode_1)]
            n2 = numbers[get_index(numbers, i + 2, mode_2)]
            numbers[get_index(numbers, i + 3, mode_3)] = n1 * n2
            increase_amount = 4
        elif n == 3:
            numbers[get_index(numbers, i + 1, mode_1)] = input[j]
            j += 1
            increase_amount = 2
        elif n == 4:
            result = numbers[get_index(numbers, i + 1, mode_1)]
            increase_amount = 2
            return result, i + increase_amount
        elif n == 5:
            condition_value = numbers[get_index(numbers, i + 1, mode_1)]
            if int(condition_value) != 0:
                i = numbers[get_index(numbers, i + 2, mode_2)]
                increase_amount = 0
            else:
                increase_amount = 3
        elif n == 6:
            condition_value = numbers[get_index(numbers, i + 1, mode_1)]
            if int(condition_value) == 0:
                i = numbers[get_index(numbers, i + 2, mode_2)]
                increase_amount = 0
            else:
                increase_amount = 3
        elif n == 7:
            numbers[get_index(numbers, i + 3, mode_3)] = 1 if int(numbers[get_index(numbers, i + 1, mode_1)]) < int(numbers[get_index(numbers, i + 2, mode_2)]) else 0
            increase_amount = 4
        elif n == 8:
            numbers[get_index(numbers, i + 3, mode_3)] = 1 if int(numbers[get_index(numbers, i + 1, mode_1)]) == int(numbers[get_index(numbers, i + 2, mode_2)]) else 0
            increase_amount = 4
        else:
            print("Error!")
            break
        i += increase_amount
    return result, i


def get_index(numbers, i, parameter_mode):
    return i if int(parameter_mode) == 1 else numbers[i]


if __name__ == "__main__":
    main()
