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
        num_rolls = int(input('How many times do you want to roll the die? '))

    # "rolls" die number of times and presents output
    roll_die(num_rolls)


def roll_die(num_rolls):
    for roll in range(1, num_rolls + 1):
        # determine roll number
        roll_number = random.randint(1, 20)
        # determine roll symbol/effect
        roll_symbol = ''
        if roll_number == 20:
            roll_symbol = 'CRITICAL HIT'
        else:
            if roll_number % 4 == 0:
                roll_symbol = 'Sword'
            elif roll_number % 4 == 1:
                roll_symbol = 'Shield'
            elif roll_number % 4 == 2:
                roll_symbol = 'Spell'
            elif roll_number % 4 == 3:
                roll_symbol = 'Potion'
        # output roll result
        print(f'Roll {roll}: {roll_number} ===> {roll_symbol}')


# run program
main()
