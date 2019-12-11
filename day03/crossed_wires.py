def sequence_breaker(sequence):
    '''Create a set of intersections, this will eliminate duplicates.
    '''
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
    '''Generator of steps.
    '''
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
    return False


def closest_intersection():
    with open('input301.txt', 'r') as sequence:
        first = sequence.readline()
        second = sequence.readline()

        grid_1 = sequence_breaker(first)
        grid_2 = sequence_breaker(second)

        grid_intersection = grid_1.intersection(grid_2)
        result = [abs(x[0]) + abs(x[1]) for x in grid_intersection]
        result.sort()
        return result[1]

def fewest_steps():
    with open('input301.txt', 'r') as sequence:
        first = sequence.readline()
        second = sequence.readline()

        grid_1 = sequence_breaker(first)
        grid_2 = sequence_breaker(second)

        not_here = []
        intersections = []
        option = None
        option_2 = None
        grid_intersection = grid_1.intersection(grid_2)

        for seq in grid_intersection:
            grid_y_1 = sequence_yield(first)
            grid_y_2 = sequence_yield(second)
            count_i = 0
            while(True):
                count_i = count_i + 1
                try:
                    option_2 = next(grid_y_2)
                except StopIteration:
                    break
                if option_2 in grid_1 and option_2 not in not_here and count_i > 1:
                    break

            count_j = 0
            while(True):
                count_j = count_j + 1
                try:
                    option = next(grid_y_1)
                except StopIteration:
                    break
                if option == option_2:
                    intersections.append(count_j + count_i)
                    not_here.append(option)
                    break
        return min(intersections) - 2


if __name__ == '__main__':
    print(f'The Manhattan distance to the closest is {closest_intersection()}')
    print(f'The fewest steps to an intersectin is {fewest_steps()}')
