def main():
    part_one()
    part_two()


def part_one():
    print("Part One")
    center = (0, 0)
    with open("input.txt", "r") as input_file:
        wires = []
        for line in input_file:
            wire = set()
            actions = line.rstrip().split(",")
            coord = center
            for action in actions:
                direction = action[0]
                if direction not in ["R", "L", "U", "D"]:
                    break
                steps = int(action[1:])
                if direction == "R":
                    for i in range(0, steps):
                        coord = (coord[0] + 1, coord[1])
                        wire.add(coord)
                elif direction == "L":
                    for i in range(0, steps):
                        coord = (coord[0] - 1, coord[1])
                        wire.add(coord)
                elif direction == "U":
                    for i in range(0, steps):
                        coord = (coord[0], coord[1] + 1)
                        wire.add(coord)
                elif direction == "D":
                    for i in range(0, steps):
                        coord = (coord[0], coord[1] - 1)
                        wire.add(coord)
            wires.append(wire)
        intersections = wires[0].intersection(wires[1])
        min_dist = None
        for intersection in intersections:
            min_dist = manhattan_distance(center, intersection) if min_dist is None else min(min_dist, manhattan_distance(center, intersection))
        print("Distance: ", min_dist)


def part_two():
    print("Part Two")
    center = (0, 0)
    with open("input.txt", "r") as input_file:
        wires = []
        timings = []
        for line in input_file:
            wire = set()
            timing = dict()
            time = 0
            actions = line.rstrip().split(",")
            coord = center
            for action in actions:
                direction = action[0]
                if direction not in ["R", "L", "U", "D"]:
                    break
                steps = int(action[1:])
                if direction == "R":
                    for i in range(0, steps):
                        coord = (coord[0] + 1, coord[1])
                        time += 1
                        timing[str(coord)] = timing.get(str(coord), time)
                        wire.add(coord)
                elif direction == "L":
                    for i in range(0, steps):
                        coord = (coord[0] - 1, coord[1])
                        time += 1
                        timing[str(coord)] = timing.get(str(coord), time)
                        wire.add(coord)
                elif direction == "U":
                    for i in range(0, steps):
                        coord = (coord[0], coord[1] + 1)
                        time += 1
                        timing[str(coord)] = timing.get(str(coord), time)
                        wire.add(coord)
                elif direction == "D":
                    for i in range(0, steps):
                        coord = (coord[0], coord[1] - 1)
                        time += 1
                        timing[str(coord)] = timing.get(str(coord), time)
                        wire.add(coord)
            wires.append(wire)
            timings.append(timing)
        intersections = wires[0].intersection(wires[1])
        min_timing = None
        for intersection in intersections:
            min_timing = timings[0][str(intersection)] + timings[1][str(intersection)] if min_timing is None else min(min_timing, timings[0][str(intersection)] + timings[1][str(intersection)])
        print("Distance: ", min_timing)


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


if __name__ == "__main__":
    main()
