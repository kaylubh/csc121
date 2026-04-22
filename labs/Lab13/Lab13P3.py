# Caleb Hemphill
# 04/22/2026
# Calculates the number of possible permutations and combinations
# Gets input for number of total and chosen elements
#

def get_input():
    """
    Gets input from the user for number of total elements and chosen elements. Validates the input for both is a
    positive integer greater than 0. Validates the input for chosen elements is less than the number of total elements.
    :return: tuple(int, int): total_elements, chosen_elements
    """
    total_elements = 0
    chosen_elements = 0

    # Gets and validates input for number of total elements, loops until input is valid
    invalid_total_elements = True
    while invalid_total_elements:
        try:
            total_elements = int(input("Number of total elements? "))
        except ValueError:
            print('Number of total elements must be a positive integer greater than 0')
        else:
            if total_elements > 0:
                invalid_total_elements = False
            else:
                print('Number of total elements must be a positive integer greater than 0')

    # Gets and validates input for number of chosen elements, loops until input is valid
    invalid_chosen_elements = True
    while invalid_chosen_elements:
        try:
            chosen_elements = int(input("Number of chosen elements? "))
        except ValueError:
            print('Number of chosen elements must be a positive integer greater than 0')
        else:
            if 0 < chosen_elements < total_elements:
                invalid_chosen_elements = False
            else:
                print('Number of chosen elements must be a positive integer greater than 0 and less than the '
                      'number of total elements')

    return total_elements, chosen_elements


def factorial(number):
    """
    Returns the factorial of number
    :param number:
    :return: integer
    """
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def calculate_permutations(n, r):
    """
    Calculates the number of permutations given the total number of elements and the number of chosen elements.
    :param n: total number of elements
    :param r: number of chosen elements
    :return: integer: number of permutations
    """
    return int(factorial(n) / factorial(n - r))


def calculate_combinations(n, r):
    """
    Calculates the number of combinations given the total number of elements and the number of chosen elements.
    :param n: total number of elements
    :param r: number of chosen elements
    :return: integer: number of combinations
    """
    return int(factorial(n) / (factorial(r) * factorial(n - r)))


def main():
    """
    Calculates and displays the number of permutations and combinations using input from the user for the total
    number of elements and number of chosen elements.
    :return:
    """
    # Get user input
    total_elements, chosen_elements = get_input()

    # Calculate permutations and calculations
    permutations = calculate_permutations(total_elements, chosen_elements)
    combinations = calculate_combinations(total_elements, chosen_elements)

    # Display output
    print('----------')
    print(f'Number of total elements: {total_elements}')
    print(f'Number of chosen elements: {chosen_elements}')
    print(f'\t Permutations: P({total_elements},{chosen_elements}) = {permutations}')
    print(f'\t Combinations: C({total_elements},{chosen_elements}) = {combinations}')


main()
