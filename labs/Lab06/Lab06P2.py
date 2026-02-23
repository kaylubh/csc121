#
# Caleb Hemphill
# 02/23/2026
# Tuple Random Number Generator
#

import random


def main():
    # Step A
    print('Step A:')
    length = int(input('How many values to put in the tuple? '))

    # Step B
    print('Step B:')
    lower_limit = int(input('What is the start of the range? '))
    upper_limit = int(input('What is the end of the range? '))

    # Step C
    print('Step C:')
    random_numbers = tuple([random.randint(lower_limit, upper_limit) for _ in range(length)])
    print(f'Tuple of {length} random numbers: {random_numbers}')

    # Step D
    print('Step D:')
    first_4_numbers = random_numbers[:4]
    print(f'Tuple of first 4 numbers: {first_4_numbers}')

    # Step E
    print('Step E:')
    last_2_numbers = random_numbers[-2:]
    print(f'Tuple of last 2 numbers: {last_2_numbers}')

    # Step F
    print('Step F:')
    concatenated_numbers = last_2_numbers + first_4_numbers
    print(f'Two tuples concatenated: {concatenated_numbers}')

    # Step G
    print('Step G:')
    concatenated_incremented_numbers = tuple([number + 1 for number in concatenated_numbers])
    print(f'Two tuples concatenated and incremented: {concatenated_incremented_numbers}')


if __name__ == '__main__':
    main()
