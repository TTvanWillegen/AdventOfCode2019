import sys


def main():
    part_one()
    part_two()


def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return None


def ratio(x1, x2):
    delta_x = x2[0] - x1[0]
    delta_y = x2[1] - x1[1]
    if delta_y == 0:
        return sign(delta_x), sign(delta_y), None
    return sign(delta_x), sign(delta_y), float(delta_x) / float(delta_y)


def part_one():
    print("Part One")
    with open("input.txt", "r") as input_file:
        asteroids = []

        x = 0
        y = 0
        for line in input_file:
            for point in line:
                if point == "#":
                    asteroids += [(x, y)]
                x += 1
            y += 1
            x = 0

        asteroids_view = dict()
        view_counter = dict()
        for asteroid in asteroids:
            views = asteroids_view.get(asteroid, [])
            for other in asteroids:
                if asteroid == other:
                    continue
                view = ratio(asteroid, other)
                if view not in views:
                    views += [view]
                    count = view_counter.get(asteroid, 0)
                    count += 1
                    view_counter[asteroid] = count
                    asteroids_view[asteroid] = views

        max_count = 0
        max_location = None
        for asteroid in asteroids:
            counter = view_counter.get(asteroid, 0)
            if max_count < counter:
                max_count = counter
                max_location = asteroid
        print(max_count, max_location)


def part_two():
    with open("input.txt", "r") as input_file:
        asteroids = []

        x = 0
        y = 0
        size_x = 0
        size_y = 0
        for line in input_file:
            for point in line:
                if point == "#":
                    asteroids += [(x, y)]
                x += 1
            y += 1
            size_y = y
            size_x = x
            x = 0

        ratios_view = dict()
        asteroid_view = dict()
        view_counter = dict()
        for asteroid in asteroids:
            views = ratios_view.get(asteroid, [])
            viewable_asteroids = asteroid_view.get(asteroid, [])
            for other in asteroids:
                if asteroid == other:
                    continue
                view = ratio(asteroid, other)
                if view not in list(map(lambda v: v[0], views)):
                    # if there are no listed asteroids in this direction yet, add these.
                    count = view_counter.get(asteroid, 0)
                    view_counter[asteroid] = count + 1

                    views += [(view, other, (other[0] - asteroid[0], other[1] - asteroid[1]))]
                    ratios_view[asteroid] = views

                    viewable_asteroids += [other]
                    asteroid_view[asteroid] = viewable_asteroids
                else:
                    # if there are multiple asteroids in the same line; take the closest.
                    other_view = list(filter(lambda v: v[0] == view, views))[0]
                    views = list(filter(lambda v: v[0] != view, views))
                    if (abs(other[0] - asteroid[0]) + abs(other[1]-asteroid[1])) < (abs(other_view[1][0] - asteroid[0]) + abs(other_view[1][1] - asteroid[1])):
                        views += [(view, other, (other[0] - asteroid[0], other[1] - asteroid[1]))]
                    else:
                        views += [other_view]


        max_count = 0
        max_location = None
        for asteroid in asteroids:
            counter = view_counter.get(asteroid, 0)
            if max_count < counter:
                max_count = counter
                max_location = asteroid
        print(max_count, max_location)

        q1 = list(sorted(filter(lambda a: (a[0][0] == 0 or a[0][0] == 1) and a[0][1] == -1, ratios_view.get(max_location)), key=sort_list, reverse=True))
        q2 = list(sorted(filter(lambda a: a[0][0] == 1 and (a[0][1] == 0 or a[0][1] == 1), ratios_view.get(max_location)), key=sort_list, reverse=True))
        q3 = list(sorted(filter(lambda a: (a[0][0] == 0 or a[0][0] == -1) and a[0][1] == 1, ratios_view.get(max_location)), key=sort_list, reverse=True))
        q4 = list(sorted(filter(lambda a: a[0][0] == -1 and (a[0][1] == 0 or a[0][1] == -1), ratios_view.get(max_location)), key=sort_list, reverse=True))

        print(q1)
        print(q2)
        print(q3)
        print(q4)

        q = q1 + q2 + q3 + q4
        print(len(q), q)
        i = 1
        for x in q:
            print(i, x)
            i += 1

        for y in range(size_y):
            for x in range(size_x):
                a = (x, y)
                if a == max_location:
                    sys.stdout.write('XXX')
                elif a in asteroids:
                    j = 0
                    found = False
                    for b in q:
                        j += 1
                        if a == b[1]:
                            sys.stdout.write(str(j).zfill(3))
                            found = True
                            break
                    if not found:
                        sys.stdout.write('###')
                else:
                    sys.stdout.write('   ')
            sys.stdout.write('\n')


def sort_list(x):
    a = x[0][2]
    if a is None:
        a = 0 if sign(x[0][0] * x[0][1]) else 10000000000
    return a


if __name__ == "__main__":
    main()
