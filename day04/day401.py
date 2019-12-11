"""
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

- It is a six-digit number.
- The value is within the range given in your puzzle input.
- Two adjacent digits are the same (like 22 in 122345).
- Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

- 111111 meets these criteria (double 11, never decreases).
- 223450 does not meet these criteria (decreasing pair of digits 50).
- 123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 284639-748759.
"""

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
    print('NEW GROUP')
    print(number)
    print(groups)
    print(2 in groups)
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
    print(len(passwords))

