def validate_sequence(number):
    for i, j in enumerate(number):
        if i + 2 > len(number) or j <= number[i + 1]:
            continue
        else:
            return False
    return True


def validate_doubles(number):
    for i, j in enumerate(number):
        if i + 2 > len(number):
            break
        if j == number[i + 1]:
            return True
    return False


def validate_double(number):
    groups = []
    count = 1
    for i, j in enumerate(number):
        if i + 2 > len(number):
            groups.append(count)
            break
        if j == number[i + 1]:
            count = count + 1
        else:
            groups.append(count)
            count = 1
    if 2 in groups:
        return True
    return False


def validate(password):
    number_sequence = list(map(int, str(password)))
    if not validate_sequence(number_sequence):
        return False
    if not validate_double(number_sequence):
        return False
    return True


def password_generator(min_range, max_range):
    return [generated for generated in range(min_range, max_range) if validate(generated)]


if __name__ == '__main__':
    passwords = password_generator(284639, 748759)
    print(f'Different passwords {len(passwords)}')

