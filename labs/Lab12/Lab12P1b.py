#
# Caleb Hemphill
# 04/15/2026
# Inheritance and Polymorphism - Problem 1b
# Creates objects using InventoryItem subclasses with user input
#

from book import Book
from game import Game
from dvd import DVD


def main():
    items = []

    # create items and get input
    for _ in range(3):
        new_item = Book()  # defaults to book item
        item_type = int(input('What item type (1-Book, 2-Game, 3-DVD)? '))

        if item_type == 1:
            new_item = Book()
        if item_type == 2:
            new_item = Game()
        if item_type == 3:
            new_item = DVD()

        new_item.get_item_input()
        items.append(new_item)
        print('')

    # display items
    for item in items:
        print(item)


main()
