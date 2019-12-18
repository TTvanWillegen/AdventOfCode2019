def main():
    part_one()
    part_two()


def part_one():
    print("Part One")
    with open("input.txt", "r") as input_file:
        for line in input_file:
            print(line)
            if len(line.rstrip()) == 0:
                continue


def part_two():
    print("Part Two")


if __name__ == "__main__":
    main()
