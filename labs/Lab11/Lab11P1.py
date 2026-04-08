#
# Caleb Hemphill
# 04/08/2026
# Uses the InventoryItem class to create and print items
#

from inventory_item import InventoryItem


def main():
    # create 3 InventoryItems and print them
    python_for_all = InventoryItem('Python for All', 10, 12.95, 'Book')
    barbie = InventoryItem('Barbie', 15, 6.95, 'DVD')
    uno = InventoryItem('Uno', 32, 4.50, 'Game')

    print(python_for_all)
    print(barbie)
    print(uno)
    print()

    # create a new empty InventoryItem, prompt the user for items details, and print it
    new_item = InventoryItem()
    new_item.get_item_input()

    print()
    print(new_item)


main()
