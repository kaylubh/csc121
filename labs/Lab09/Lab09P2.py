#
# Caleb Hemphill
# 03/25/26
# Set methods/practice
#

import random


def main():
    """
    Creates two sets using 8 random integers between 1 and 16. Uses those sets to perform various set specific methods
    to demonstrate the use of sets. Displays all results to the user in the console.
    :return:
    """

    # create and display two sets of random integers
    set1 = set([random.randint(1, 16) for _ in range(8)])
    set2 = set([random.randint(1, 16) for _ in range(8)])

    print(f'set1: {set1}')
    print(f'set2: {set2}')

    # display the union of the sets
    union_set = set1.union(set2)

    print(f'Union of set1 and set2: {union_set}')

    # display the intersectin of the sets
    intersection_set = set1.intersection(set2)

    print(f'Intersection of set1 and set2: {intersection_set}')

    # display the difference of set1 to set2
    difference_set = set1.difference(set2)

    print(f'Difference of set1 and set2: {difference_set}')

    # display the symmetric difference of the sets
    symmetric_difference_set = set1.symmetric_difference(set2)

    print(f'Symmetric difference of set1 and set2: {symmetric_difference_set}')

    # display a set comprehension of numbers < 10 from the union set
    set_comprehension = {num for num in union_set if num < 10}

    print(f'Less than 10 in union of set1 and set2: {set_comprehension}')


main()
