import sys
from functools import reduce


def main():
    part_one()
    part_two()


def part_one():
    print("Part One")
    with open("input.txt", "r") as input_file:
        for line in input_file:
            rows = 6
            columns = 25
            layers = []
            x = 0
            while x < len(line):
                layers.append(line[x: x + (rows * columns)])
                x += rows * columns

            min_0 = rows * columns + 1
            min_index = 0
            i = 0
            for x in layers:
                if x.count("0") < min_0:
                    min_0 = x.count("0")
                    min_index = i
                i += 1
            print(layers[min_index].count("1") * layers[min_index].count("2"))


def part_two():
    print("Part Two")
    with open("input.txt", "r") as input_file:
        for line in input_file:
            rows = 6
            columns = 25
            layers = []
            x = 0
            while x < len(line):
                layers.append(line[x: x + (rows * columns)])
                x += rows * columns

            image = reduce(reduce_string, layers)
            i = 0
            while i < len(image):
                if i % 25 == 0:
                    sys.stdout.write('\n')

                if image[i] == "2":
                    sys.stdout.write(' ')
                elif image[i] == "1":
                    sys.stdout.write('█')
                elif image[i] == "0":
                    sys.stdout.write('░')
                i += 1


def reduce_string(x, y):
    final = ""
    for i in range(len(x)):
        if x[i] == "0" or x[i] == "1":
            final += x[i]
        else:
            final += y[i]
    return final


if __name__ == "__main__":
    main()
