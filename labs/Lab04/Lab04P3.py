##
# Caleb Hemphill
# 02/09/2026
# Special Die Roll Simulator
#

import random

def main():
    # get input for number of rolls and validate it is between 5-15
    num_rolls = int(input('How many times do you want to roll the die? '))
    while num_rolls < 5 or num_rolls > 15:
        print('Enter a number between 5 and 15.')
        num_rolls= int(input('How many times do you want to roll the die? '))

    # "rolls" die number of times and presents output
    roll_die(num_rolls)

def roll_die(num_rolls):
    for roll in range(1, num_rolls + 1):
        # determine roll number
        roll_value = random.randint(1, 20)
        # determine roll symbol/effect

        # output roll result
        print(f'Roll {roll}: {roll_value}')

# run program
main()