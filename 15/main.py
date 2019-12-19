import time
from functools import reduce
from queue import Queue
from random import randrange


def main():
    part_one()
    # part_two()


def part_one():
    print("Part One")
    with open("input.txt", "r") as input_file:
        for line in input_file:
            if len(line.rstrip()) == 0:
                continue
            print("Parsing ", line)
            numbers = list(map(int, line.split(",")))
            numbers = numbers + ([0] * 150)
            print(numbers)
            i = 0
            relative_base = 0
            currentMovement = 1
            leftTurn = False
            currentPosition = (0, 0)
            world = {(0, 0): "╬"}
            worldReversed = {"╬": (0, 0)}
            oxygen = {}
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
                    fw = getForward(currentPosition, currentMovement)
                    isWall = world.get(fw, "") == "▒"
                    if leftTurn:
                        leftTurn = False
                        currentMovement = moveLeft(currentMovement)
                    elif isWall:
                        while isWall:
                            fw = getForward(currentPosition, currentMovement)
                            isWall = world.get(fw, "") == "▒"
                            if isWall:
                                currentMovement = moveRight(currentMovement)
                    else:
                        leftTurn = True

                    numbers[get_index(numbers, relative_base, i + 1, mode_1)] = currentMovement
                    increase_amount = 2
                elif n == 4:
                    result = int(numbers[get_index(numbers, relative_base, i + 1, mode_1)])

                    obj = "X"
                    if result == 0:
                        obj = "▒"
                    elif result == 1:
                        obj = " "
                    elif result == 2:
                        obj = "O"
                        worldReversed["O"] = getForward(currentPosition, currentMovement)
                    if currentMovement == 1:
                        world[(currentPosition[0], currentPosition[1] - 1)] = obj
                    elif currentMovement == 2:
                        world[(currentPosition[0], currentPosition[1] + 1)] = obj
                    elif currentMovement == 3:
                        world[(currentPosition[0] - 1, currentPosition[1])] = obj
                    elif currentMovement == 4:
                        world[(currentPosition[0] + 1, currentPosition[1])] = obj

                    if result != 0:
                        currentPosition = getForward(currentPosition, currentMovement)

                    # print_world_map(world, currentPosition)
                    if currentPosition == (0, 0) and result != 0:
                        break
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
            print_world_map(world, currentPosition)
            bfs = Queue()
            bfs.put(worldReversed.get("O"))
            oxygen[worldReversed.get("O")] = 0
            while not bfs.empty():
                current = bfs.get()
                currentOxygen = oxygen.get(current)
                neighbours = getNeighbours(world, current, oxygen.keys())
                for neighbour in neighbours:
                    oxygen[neighbour] = currentOxygen + 1
                    bfs.put(neighbour)
            print(oxygen)
            print(oxygen.get((0,0)))
            print(reduce(lambda i, o: max(i, oxygen.get(o)), oxygen, 0))


def getNeighbours(world, currentPosition, alreadyDone):
    todo = []
    p1 = (currentPosition[0], currentPosition[1] + 1)
    p2 = (currentPosition[0], currentPosition[1] - 1)
    p3 = (currentPosition[0] + 1, currentPosition[1])
    p4 = (currentPosition[0] - 1, currentPosition[1])
    if p1 not in alreadyDone and world.get(p1, "▒") == " ":
        todo += [p1]
    if p2 not in alreadyDone and world.get(p2, "▒") == " ":
        todo += [p2]
    if p3 not in alreadyDone and world.get(p3, "▒") == " ":
        todo += [p3]
    if p4 not in alreadyDone and world.get(p4, "▒") == " ":
        todo += [p4]
    return todo


def part_two():
    print("Part Two")
    print("See last line part_one()")


def moveRight(currentMovement):
    if currentMovement == 1:
        return 4
    elif currentMovement == 2:
        return 3
    elif currentMovement == 3:
        return 1
    elif currentMovement == 4:
        return 2


def moveLeft(currentMovement):
    if currentMovement == 1:
        return 3
    elif currentMovement == 2:
        return 4
    elif currentMovement == 3:
        return 2
    elif currentMovement == 4:
        return 1


def getForward(currentPosition, currentMovement):
    fw = None
    if currentMovement == 1:
        fw = (currentPosition[0], currentPosition[1] - 1)
    elif currentMovement == 2:
        fw = (currentPosition[0], currentPosition[1] + 1)
    elif currentMovement == 3:
        fw = (currentPosition[0] - 1, currentPosition[1])
    elif currentMovement == 4:
        fw = (currentPosition[0] + 1, currentPosition[1])
    return fw


def print_world_map(world, current_location):
    min_x = reduce(lambda i, o: min(i, o[0]), world, 0)
    max_x = reduce(lambda i, o: max(i, o[0]), world, 0)
    min_y = reduce(lambda i, o: min(i, o[1]), world, 0)
    max_y = reduce(lambda i, o: max(i, o[1]), world, 0)
    for y in range(min_y, max_y + 2):
        for x in range(min_x, max_x + 2):
            a = (x, y)
            if a == current_location and world.get(a, None) == "O":
                print("*", end="")
            elif a == current_location:
                print("D", end="")
            else:
                print(world.get(a, "░"), end="")
        print("")


def get_index(numbers, relative_base, i, parameter_mode):
    if int(parameter_mode) == 2:
        return relative_base + numbers[i]
    elif int(parameter_mode) == 1:
        return i
    elif int(parameter_mode) == 0:
        return numbers[i]


if __name__ == "__main__":
    main()
