#
# Caleb Hemphill
# 02/02/2026
# X Pattern Generator
#

# Do not change the next line. Just ignore it.
FillThisIn = None

# Replace the FillThisIn below with correct code.
# Do not change or remove any other parts of the
# code or comments.

# Ask the user for the size of the pattern
# Use the prompt from the Sample Output.
size = int(input('Enter an odd number for the size: '))

# Iterate over the rows.
for row in range(1, size + 1):
    # Iterate over the columns.
    for col in range(1, size + 1):
        # Test if the position is on the diagonal
        # Hint: Test if col and row are equal
        if col == row:
            print('*', end='')
        # Test if col and row are on the other diagonal
        # Hint: The other diagonal is where the sum of
        # the row and column indices equals the size - 1
        elif (row + col) - 1 == size:
            print('*', end='')
        else:
            print(' ', end='')

    # Go to the next row.
    print()
