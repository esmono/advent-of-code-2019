import csv

def code_1(noun, verb):
    return int(noun) + int(verb)

def code_2(noun, verb):
    return int(noun) * int(verb)

def intcode_program(sequence):
    '''Iterate the sequence in batches of 4 items.
    '''
    jump_positions = 4

    with open(sequence, 'r') as intcode_base:
        intcode_full = csv.reader(intcode_base)
        intcode = list(intcode_full)[0]
        for position in range(len(intcode) // 4):
            start = jump_positions * position
            end = (jump_positions * position) + 4
            segment = intcode[start:end]
            if len(segment) != 4:
                print('NO GO')
            if segment[0] == '1':
                intcode[int(segment[3])] = code_1(intcode[int(segment[1])],
                                                  intcode[int(segment[2])])
            elif segment[0] == '2':
                intcode[int(segment[3])] = code_2(intcode[int(segment[1])],
                                                  intcode[int(segment[2])])
            elif segment[0] == '99':
                # Halt execution
                break
            else:
                print('FALSE')
        return intcode[0]


if __name__ == '__main__':
    print(f'The valuo at position 0 is {intcode_program("input201.txt")}')
    print(f'The valuo at position 0 is {intcode_program("input202.txt")}')
