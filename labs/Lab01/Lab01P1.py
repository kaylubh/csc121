#
# Caleb Hemphill
# 01/14/2026
# Example program for receiving input from and displaying out to the terminal
#

import datetime

name = input('What is your name? ')
print(f'Welcome to CSC121 {name}!')
print(f'Today is {datetime.date.today():%B %d, %Y}')
print('I hope you learn a lot of Python this semester!')
