#
# Caleb Hemphill
# 04/15/2026
# Inheritance and Polymorphism - Problem 1a
# Creates objects using InventoryItem subclasses
#

from book import Book
from game import Game
from dvd import DVD


def main():
    book1 = Book('Python Now', 100, 22.95, '2345234523451')
    book2 = Book('Even More Python', 150, 22.95, '3456345634561')
    game1 = Game('Uno', 75, 6.95, '123456789012')
    dvd1 = DVD('Barbie', 50, 12.00, '098765432121', 'Comedy')
    dvd2 = DVD('The Piano', 10, 2.90, '321321321321', 'Drama')

    print(book1)
    print(book2)
    print(game1)
    print(dvd1)
    print(dvd2)


main()
