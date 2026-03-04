#
# Caleb Hemphill
# 03/03/2026
# String manipulation practice
#

import os

# DO NOT CHANGE ANY CODE IN THE MAIN FUNCTION
def main():
    try:
        input_file = open('strings.txt', 'r')  # Open a file for reading
        for line in input_file:  # Use a for loop to read each line in the file
            manipulate_text(line)
            print()
    except FileNotFoundError:
        print('Did not find strings.txt in current directory:')
        print(os.getcwd())


def manipulate_text(line):
    """
    This function accepts a string, performs various manipulations on the
    string, and outputs the results. It demonstrates many different str
    methods, operators, and functions from Lesson 7 of CSC-121.

    :param line: A text string to be manipulated
    :return:
    """

    # Strip the leading and trailing whitespace, and output the string.
    line = line.strip()
    print(f'Original line: {line}')

    # Replace all occurrences of $NAME with your first name.
    line = line.replace('$NAME', 'Caleb')

    # Replace all occurrences of $EMAIL with your email address.
    line = line.replace('$EMAIL', 'cbhemphill@my.waketech.edu')

    # Replace all occurrences of $CITY with the name of the city where you live.
    line = line.replace('$CITY', 'Raleigh, NC')

    # Print the updated line.
    print(f'Updated line: {line}')

    # Print a message indicating the number of characters in the updated line.
    line_length = len(line)
    print(f'Number of characters in updated line: {line_length}')

    # Count the number of occurrences of your first name and print a message
    # reporting the count.
    print(f'Occurrences of Caleb: {line.count("Caleb")}')

    # Use floor division to divide the number of characters by 2, then print
    # the first half and last half of the line.
    half_line_length = line_length // 2
    print(f'First half of line: {line[:half_line_length]}')
    print(f'Second half of line: {line[half_line_length:]}')

    # Print the line in uppercase.
    print(f'Line in uppercase: {line.upper()}')

    # Print the line in lowercase.
    print(f'Line in lowercase: {line.lower()}')


main()
