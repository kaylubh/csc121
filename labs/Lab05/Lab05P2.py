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

    # Step A
    print('Step A:')
    list_length = int(input('How many numbers in each list? '))

    # Step B
    print('Step B:')
    number_lower_bound = int(input('What is the lower bound for the random number? '))
    number_upper_bound = int(input('What is the upper bound for the random number? '))

    # Step C
    print('Step C:')
    list_1 = generate_random_list(list_length, number_lower_bound, number_upper_bound)
    print(f'First List: {list_1}')

    # Step D
    print('Step D:')
    list_2 = generate_random_list(list_length, number_lower_bound, number_upper_bound)
    print(f'Second List: {list_2}')

    # Step E
    print('Step E:')
    print('List Pairs:')
    for i in range(len(list_1)):
        print(f'{list_1[i]} {list_2[i]}')

    # Step F
    print('Step F:')
    combined_list = list_1 + list_2
    print(f'Combined List: {combined_list}')

    # Step G
    print('Step G:')
    combined_list.sort()
    print(f'Sorted List: {combined_list}')

    # Step H
    print('Step H:')
    print(f'First Three Elements: {combined_list[:3]}')
    print(f'Last Three Elements: {combined_list[-3:]}')

    # Step I
    print('Step I:')
    print(f'Sum: {sum(combined_list)}')

    # Step J
    print('Step J:')
    print(f'Minimum: {min(combined_list)}')

    # Step K
    print('Step K:')
    print(f'Maximum: {max(combined_list)}')

    # Step L
    print('Step L:')
    print('Remove Random Values:')
    remove_list = generate_random_list(5, number_lower_bound, number_upper_bound)
    for element in remove_list:
        if element in combined_list:
            print(f'{element} at index {combined_list.index(element)}')
            combined_list.remove(element)
        else:
            print(f'{element} not found in list')

    # Step M
    print('Step M:')
    print(f'Final List: {combined_list}')


main()
