#
# Caleb Hemphill
# 02/02/2026
# Calculates the totals and tax for an order
# Input validation for negative numbers and quantity limits
#

# Prices
BOOK_PRICE = 2.25
DVD_PRICE = 4.35
GAME_PRICE = 5.00
SALES_TAX = 0.065

# Maximum Quantities
MAX_BOOKS = 30
MAX_DVDS = 15
MAX_GAMES = 10

# Input
# gets number of each item being purchased
# validates input to not accept negative numbers or numbers above the quantity limit
num_books = int(input('Enter the number of books: '))
while num_books < 0 or num_books > MAX_BOOKS:
    print('Number of books must be between 0 and 30.')
    num_books = int(input('Enter the number of books: '))

num_dvds = int(input('Enter the number of DVDs: '))
while num_dvds < 0 or num_dvds > MAX_DVDS:
    print('Number of DVDs must be between 0 and 15.')
    num_dvds = int(input('Enter the number of DVDs: '))

num_games = int(input('Enter the number of games: '))
while num_games < 0 or num_games > MAX_GAMES:
    print('Number of games must be between 0 and 10.')
    num_games = int(input('Enter the number of games: '))

# Processing
# totals the order purchase price
subtotal = (num_books * BOOK_PRICE) + (num_dvds * DVD_PRICE) + (num_games * GAME_PRICE)
tax = subtotal * SALES_TAX
total = subtotal + tax

# Output
# outputs totals to user
print('--------------------')
print(f'Cost before tax: ${subtotal:.2f}')
print(f'Sales tax: ${tax:.2f}')
print(f'Cost after tax: ${total:.2f}')
