#
# Caleb Hemphill
# 02/16/2026
# Random List Generator
#

import random


def generate_random_list(list_length, lower_bound, upper_bound):
    """
    Creates a list of random numbers of the specified list_length.
    Each element will be an integer with a value between lower_bound and upper_bound
    :param list_length: length of list to be generated
    :param lower_bound: maximum value of each element
    :param upper_bound: minimum value of each element
    :return: list of random integers
    """

    random_list = []

    # create list elements and assign a random number within bounds
    for _ in range(list_length):
        random_list.append(random.randint(lower_bound, upper_bound))

    return random_list


def main():
    list_1 = []
    list_2 = []

    # Step A
    print('Step A:')
    list_length = int(input('\tHow many numbers in each list? '))

    # Step B
    print('Step B:')
    number_lower_bound = int(input('\tWhat is the lower bound for the random number? '))
    number_upper_bound = int(input('\tWhat is the upper bound for the random number? '))

    # Step C
    print('Step C:')
    list_1 = generate_random_list(list_length, number_lower_bound, number_upper_bound)
    print(f'\tFirst List: {list_1}')

    # Step D
    print('Step D:')
    list_2 = generate_random_list(list_length, number_lower_bound, number_upper_bound)
    print(f'\tFirst List: {list_2}')


main()
