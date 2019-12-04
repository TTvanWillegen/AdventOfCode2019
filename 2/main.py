def main():
    # 1 add
    # 2 multiply
    # 99 halt
    # What value is at position 0
    part_one()
    part_two()


def part_one():
    print("Part One")
    with open("input.txt", "r") as input_file:
        for line in input_file:
            numbers = list(map(int, line.split(",")))

            # Restore
            numbers[1] = 12
            numbers[2] = 2

            i = 0
            while i < len(numbers):
                n = numbers[i]
                if n == 99:
                    break
                n1 = numbers[numbers[i + 1]]
                n2 = numbers[numbers[i + 2]]
                if n == 1:
                    result = n1 + n2
                elif n == 2:
                    result = n1 * n2
                else:
                    print("Error!")
                    break
                numbers[numbers[i + 3]] = result
                i += 4
            print(numbers[0], numbers)


def part_two():
    print("Part Two")
    with open("input.txt", "r") as input_file:
        for line in input_file:
            for i_noun in range(0, 100):
                for i_verb in range(0, 100):
                    numbers = list(map(int, line.split(",")))

                    numbers[1] = i_noun
                    numbers[2] = i_verb

                    i = 0
                    while i < len(numbers):
                        n = numbers[i]
                        if n == 99:
                            break
                        noun = numbers[numbers[i + 1]]
                        verb = numbers[numbers[i + 2]]
                        if n == 1:
                            result = noun + verb
                        elif n == 2:
                            result = noun * verb
                        else:
                            print("Error!")
                            break
                        numbers[numbers[i + 3]] = result
                        i += 4
                    if numbers[0] == 19690720:
                        print(numbers[0], " = 100 * ", i_noun, " * ", i_verb, numbers)


if __name__ == "__main__":
    main()
