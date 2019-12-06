def main():
    part_one()
    part_two()


def part_one():
    print("Part One")
    with open("input.txt", "r") as input_file:
        orbits = dict()
        for line in input_file:
            (a, b) = line.rstrip().split(")")
            orbit_set = orbits.get(a, set())
            orbit_set.add(b)
            orbits[a] = orbit_set
        amounts = get_number(orbits, "COM", 0)
        total = 0
        for item in amounts:
            total += amounts[item]
        print(total)


def get_number(orbits, name, i):
    this_orbits = orbits.get(name, [])
    if len(this_orbits) == 0:
        return dict({name: i})
    else:
        amounts = dict()
        for orbit in this_orbits:
            amounts[orbit] = i + 1
            amounts = {**amounts, **get_number(orbits, orbit, i + 1)}
        return amounts


def part_two():
    print("Part Two")
    with open("input.txt", "r") as input_file:
        orbits = dict()
        orbits_around = dict()
        for line in input_file:
            (a, b) = line.rstrip().split(")")
            orbit_set = orbits.get(a, set())
            orbit_set.add(b)
            orbits[a] = orbit_set
            orbits_around[b] = a
        intersect = it(orbits_around, "SAN").intersection(it(orbits_around, "YOU"))
        print(intersect)
        print(it2(orbits_around, "SAN", intersect) + it2(orbits_around, "YOU", intersect) - 2)


def it(orbits, a):
    if a == "COM":
        return {"COM"}
    else:
        s = it(orbits, orbits[a])
        s.add(str(a))
        return s


def it2(orbits, a, final):
    if a in final:
        return 0
    else:
        return it2(orbits, orbits[a], final) + 1


if __name__ == "__main__":
    main()
