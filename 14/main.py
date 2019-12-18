from collections import namedtuple
from functools import reduce
from math import ceil

Element = namedtuple("Element", ["amount", "type"])


def main():
    part_one()
    part_two()


def part_one():
    print("Part One")
    with open("input.txt", "r") as input_file:
        levels = {"ORE": 0}
        reactions = dict()
        for line in input_file:
            if len(line.rstrip()) == 0:
                break
            reaction = line.rstrip().split(" => ")
            requirements = reaction[0].split(", ")
            mappedRequirements = []
            for element in requirements:
                e = Element(int(element.split(" ")[0]), element.split(" ")[1])
                mappedRequirements.append(e)
            to_elem = reaction[1].split(" ")
            reactions[Element(int(to_elem[0]), to_elem[1])] = mappedRequirements

        # Get the levels of chemicals.
        while len(reactions) > len(levels) - 1:
            for reaction in reactions:
                if levels.get(reaction.type, None) is None:
                    maxLevel = 0
                    for e in reactions.get(reaction):
                        e_level = levels.get(e.type, None)
                        maxLevel = None if maxLevel is None or e_level is None else max(maxLevel, e_level)
                    if maxLevel is not None:
                        levels[reaction.type] = maxLevel + 1
        print(levels)
        print(reactions)

        ore = calculate_ore(reactions, levels, {"FUEL": 1})
        print("Ore:", ore)


def calculate_ore(reactions, levels, required):
    while len(required) is not 0:
        maxLevel = reduce(lambda i, o: max(levels[o], i) if required[o] != 0 else i, required, 0)
        if maxLevel == 0:
            break
        currentElem = next((x for x in required if required[x] != 0 and levels[x] == maxLevel))
        reaction = next((x for x in reactions if x.type == currentElem))
        reaction_amount = ceil(required[currentElem] / reaction.amount)
        required[currentElem] = 0
        for element in reactions[reaction]:
            required[element.type] = required.get(element.type, 0) + reaction_amount * element.amount
    return required["ORE"]


def part_two():
    print("Part Two")
    with open("input.txt", "r") as input_file:
        levels = {"ORE": 0}
        reactions = dict()
        for line in input_file:
            if len(line.rstrip()) == 0:
                break
            reaction = line.rstrip().split(" => ")
            requirements = reaction[0].split(", ")
            mappedRequirements = []
            for element in requirements:
                e = Element(int(element.split(" ")[0]), element.split(" ")[1])
                mappedRequirements.append(e)
            to_elem = reaction[1].split(" ")
            reactions[Element(int(to_elem[0]), to_elem[1])] = mappedRequirements

        # Get the levels of chemicals.
        while len(reactions) > len(levels) - 1:
            for reaction in reactions:
                if levels.get(reaction.type, None) is None:
                    maxLevel = 0
                    for e in reactions.get(reaction):
                        e_level = levels.get(e.type, None)
                        maxLevel = None if maxLevel is None or e_level is None else max(maxLevel, e_level)
                    if maxLevel is not None:
                        levels[reaction.type] = maxLevel + 1

        ore_limit = 1000000000000
        right = 1000000000000
        left = 1
        best = 0
        while left <= right:
            mid = int((left + right) / 2)
            required_ore = calculate_ore(reactions, levels, {"FUEL": mid})
            if required_ore < ore_limit:
                best = max(best, mid)
                left = mid + 1
            elif required_ore > ore_limit:
                right = mid - 1
            else:
                best = mid
        print(best)


if __name__ == "__main__":
    main()
