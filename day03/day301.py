"""
--- Day 3: Crossed Wires ---
The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?
"""


def sequence_breaker(sequence):
    sequence = sequence.split(',')
    x_value = 0
    y_value = 0
    grid = set()

    for path in sequence:
        direction = path[0]
        distance = int(path[1:])
        if direction == 'R':
            x_value = x_value + distance
            grid.update(list(((x, y_value) for x in range(x_value - distance, x_value))))
        elif direction == 'U':
            y_value = y_value + distance
            grid.update(list(((x_value, y) for y in range(y_value - distance, y_value))))
        elif direction == 'L':
            x_value = x_value - distance
            grid.update(list(((x, y_value) for x in range(x_value + distance, x_value, -1))))
        elif direction == 'D':
            y_value = y_value - distance
            grid.update(list(((x_value, y) for y in range(y_value + distance, y_value, -1))))
        else:
            print('ERR')
    return grid


def sequence_yield(sequence):
    sequence = sequence.split(',')
    x_value = 0
    y_value = 0
    
    for path in sequence:
        direction = path[0]
        distance = int(path[1:])
        if direction == 'R':
            x_value = x_value + distance
            for x in range(x_value - distance, x_value):
                yield (x, y_value)
        elif direction == 'U':
            y_value = y_value + distance
            for y in range(y_value - distance, y_value):
                yield (x_value, y)
        elif direction == 'L':
            x_value = x_value - distance
            for x in range(x_value + distance, x_value, -1):
                yield (x, y_value)
        elif direction == 'D':
            y_value = y_value - distance
            for y in range(y_value + distance, y_value, -1):
                yield (x_value, y)
        else:
            print('ERR')
    print('END')


with open('input0301.txt', 'r') as sequence:
    first = sequence.readline()
    second = sequence.readline()

    grid_1 = sequence_breaker(first)
    grid_2 = sequence_breaker(second)

    grid_intersection = grid_1.intersection(grid_2)
    print(grid_intersection)
    result = [abs(x[0]) + abs(x[1]) for x in grid_intersection]
    result.sort()
    print(result)

    print('SECOND PART')
    not_here = []
    option = None
    option_2 = None
    for seq in grid_intersection:
        print('START ITERATION')
        grid_y_1 = sequence_yield(first)
        grid_y_2 = sequence_yield(second)
        count_i = 0
        while(True):
            count_i = count_i + 1
            option_2 = next(grid_y_2)
            if option_2 in grid_1 and option_2 not in not_here and count_i > 1:
                print(option_2, count_i)
                break

        count_j = 0
        while(True):
            count_j = count_j + 1
            option = next(grid_y_1)
            if option == option_2:
                print(option, count_j + count_i)
                not_here.append(option)
                break

