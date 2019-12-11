def module_fuel(mass, full_mass=True):
    '''Calculate the amount of fuel for each part.
    With full mass also calculate the amount of fuel for the fuel.
    '''
    fuel_mass = (mass // 3) - 2
    total = 0
    if fuel_mass <= 0:
        return total
    elif full_mass:
        total = fuel_mass + module_fuel(fuel_mass)
    else:
        total = fuel_mass
    return total


def calculate_fuel(full_mass=True):
    '''Read the file and calculate the fuel of each part.
    '''
    with open('input101.txt') as f:
        parts = f.readlines()
        test = [module_fuel(int(part.strip()), full_mass) for part in parts]
        return sum(test)


if __name__ == '__main__':
    ''' To get the amount of fuel required without adding the mass of the fuel
    pass `full_mass` as False.
    '''
    solution = calculate_fuel()
    print(f'The amount of fuel required is {solution}')
