# Caleb Hemphill
# 04/22/2026
# Display the first n Fibonacci numbers and the sum
#

def get_number():
    """
    Return a number entered by the user
    :return: the number entered by the user
    """
    while True:
        try:
            number = int(input("Enter a positive integer: "))
            if number <= 0:
                raise ValueError()
            return number
        except ValueError:
            print(f' >> Error: Enter a positive integer')


def fibonacci(n):
    """
    Return the nth Fibonacci number
    :param n: The position of the Fibonacci number
    :return: the nth Fibonacci number
    """
    # if n <= 2:
    #     return n
    # else:
    #     return fibonacci(n - 1)
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_list(n):
    """
    Create the first n numbers of the fibonacci sequence
    :param n: The length of the list to create
    :return: The list of fibonacci numbers
    """
    # return [fibonacci(i + 1) for i in range(n)]
    return [fibonacci(i) for i in range(n)]


def fibonacci_sum(fib_list):
    """
    Add the numbers in the list and return the sum
    :param fib_list: A list of fibonacci numbers
    :return: the sum of the fibonacci numbers in the list
    """
    return sum(fib_list)


def main():
    x = get_number()
    f_list = fibonacci_list(x)
    f_sum = fibonacci_sum(f_list)
    print(f' First {x} Fibonacci numbers: {f_list}')
    print(f' Sum of first {x} Fibonacci numbers is {f_sum}')


if __name__ == '__main__':
    main()
