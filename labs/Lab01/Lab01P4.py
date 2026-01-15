#
# Caleb Hemphill
# 01/14/2026
# Calculates the totals and tax for an order
# Uses hard-coded sample data for a store
#

# Prices
book_price = 2.25
dvd_price = 4.35
game_price = 5.00
sales_tax = 0.065

# Input
# gets number of each item being purchased
print('Enter the number of items in whole numbers')
num_books = int(input('Books: '))
num_dvds = int(input('DVDs: '))
num_games = int(input('Games: '))

# Processing
# totals the order purchase price
subtotal = (num_books * book_price) + (num_dvds * dvd_price) + (num_games * game_price)
tax = subtotal * sales_tax
total = subtotal + tax

# Output
# outputs totals to user
print('--------------------')
print(f'Subtotal: ${subtotal:.2f}')
print(f'Tax: ${tax:.2f}')
print(f'Total: ${total:.2f}')
