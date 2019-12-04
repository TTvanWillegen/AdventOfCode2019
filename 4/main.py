def main():
    part_one()
    part_two()


def part_one():
    print("Part One")
    with open("input.txt", "r") as input_file:
        for line in input_file:
            password_range = line.rstrip().split("-")
            counter = 0
            for i in range(int(password_range[0]), int(password_range[1])):
                success = True
                double_char = False
                last_number = None
                for number in str(i):
                    if last_number is None:
                        last_number = number
                        continue
                    if int(last_number) > int(number):
                        success = False
                        break
                    if int(last_number) == int(number):
                        last_number = number
                        double_char = True
                    if int(last_number) < int(number):
                        last_number = number
                if success:
                    counter += 1 if double_char else 0
                    print(i)
            print("N = ", counter)


def part_two():
    print("Part Two")
    with open("input.txt", "r") as input_file:
        for line in input_file:
            password_range = line.rstrip().split("-")
            counter = 0
            for i in range(int(password_range[0]), int(password_range[1])):
                success = True
                last_number = None
                double_counter = [0 for x in range(0, 10)]
                for number in str(i):
                    double_counter[int(number)] += 1
                    if last_number is None:
                        last_number = number
                        continue
                    else:
                        if int(last_number) > int(number):
                            success = False
                            break
                        if int(last_number) == int(number):
                            last_number = number
                        if int(last_number) < int(number):
                            last_number = number
                if success:
                    double_char = False
                    for x in range(0, 10):
                        double_char = double_char or double_counter[x] == 2
                    counter += 1 if double_char else 0
                    if double_char:
                        print(i)
                        print(double_counter)
            print("N = ", counter)


if __name__ == "__main__":
    main()
