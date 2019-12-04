import math


def main():
    part_one()
    part_two()


def part_one():
    with open("input.txt", "r") as input_file:
        total = 0
        for line in input_file:
            total += math.floor(int(line) / 3) - 2
        print("Part One: " + str(total))


def part_two():
    with open("input.txt", "r") as input_file:
        total = 0
        for line in input_file:
            total += calc_fuel(int(line))
        print("Part Two: " + str(total))


def calc_fuel(weight):
    if weight <= 0:
        return 0
    else:
        fuel = max(0, math.floor(int(weight) / 3) - 2)
        return fuel + calc_fuel(fuel)


if __name__ == "__main__":
    main()
