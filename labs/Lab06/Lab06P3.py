#
# Caleb Hemphill
# 02/24/2026
# List Comprehensions Practice
#

def main():
    # Step A
    print('Step A:')

    list1 = [4, 5, 8, 2]
    print(list1)

    list2 = [2, 5, 9]
    print(list2)

    # Step B
    print('Step B:')

    list3 = [number * 2 - 3 for number in range(6)]
    print(list3)

    # Step C
    print('Step C:')

    list4 = [[i, j] for i in range(4) for j in range(5) if i % 2 == 1 and j % 2 == 0]
    print(list4)

    # Step D
    print('Step D:')

    list5 = [i ** 3 for i in list1]
    print(list5)

    # Step E
    print('Step E:')

    list6 = [element * 3 for element in list1]
    print(list6)

    # Step F
    print('Step F:')

    list7 = [(list1_element * list2element) - 1 for list1_element in list1 for list2element in list2]
    print(list7)

    # Step G
    print('Step G:')

    list8 = [f'{list1_element}@{list2_element}' for list1_element in list1 for list2_element in list2]
    print(list8)


if __name__ == '__main__':
    main()
