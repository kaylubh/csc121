#
# Caleb Hemphill
# 04/19/2026
# Inheritance and Polymorphism - Problem 2
#

import pickle
from book import Book
from game import Game
from dvd import DVD


def main():
    # Calling load_inventory() should return a list of inventory items if
    # inventory.dat is present. If that file is not present, it should
    # return an empty list.
    inventory_list = load_inventory()
    display_inventory(inventory_list)

    answer_outer = ''
    while answer_outer.lower() != 'n':
        answer_inner = ''
        while answer_inner not in ['1', '2', '3']:
            answer_inner = input('What item type (1-Book, 2-Game, 3-DVD)? ')
            if answer_inner not in ['1', '2', '3']:
                print('Enter 1, 2, or 3.')

        # DONE - Create an appropriate object, ask the user for item input
        #  using the object's method, then append the object to the inventory
        #  list.

        if answer_inner == '1':
            new_book = Book()
            new_book.get_item_input()
            inventory_list.append(new_book)
        if answer_inner == '2':
            new_game = Game()
            new_game.get_item_input()
            inventory_list.append(new_game)
        if answer_inner == '3':
            new_dvd = DVD()
            new_dvd.get_item_input()
            inventory_list.append(new_dvd)

        answer_outer = input('Do you want to enter more items? ')

    display_inventory(inventory_list)
    save_inventory(inventory_list)


def load_inventory():
    """
    This function reads in a single list data structure from a
    binary file named inventory.dat and stores it in a variable
    that holds this inventory list data. The variable is returned.
    If the file does not exist, an empty list is returned.

    :return: List of all inventory objects
    """

    inventory_list = []
    # DONE - Attempt to load inventory data from a binary file named
    #  inventory.dat. If the file exists, load it into the inventory list.
    #  If the file does not exist, leave the inventory list empty.

    try:
        inventory_file = open('inventory.dat', 'rb')
        inventory_list = pickle.load(inventory_file)
        inventory_file.close()
    except FileNotFoundError:
        pass

    return inventory_list


def save_inventory(inventory_list):
    """
    This function takes the inventory list and saves it to a binary
    file named inventory.dat.

    :param inventory_list: List of all inventory objects
    :return:
    """

    # DONE - Open a binary file named inventory.dat and dump the inventory
    #  list that has been passed in as a parameter to that file.

    inventory_file = open('inventory.dat', 'wb')
    pickle.dump(inventory_list, inventory_file)
    inventory_file.close()

    print('Inventory.dat file was created.')


def display_inventory(inventory_list):
    """
    This function displays all the inventory items in the inventory.
    Each item's attributes are shown on a single line.

    :param inventory_list: List of all inventory objects
    :return:
    """

    print()
    print('Current Inventory')
    print('-----------------')
    # DONE - Display the inventory items that are in the inventory list
    #  that was passed in as a parameter. If the list is empty, display
    #  "Inventory is empty."
    if inventory_list:
        for item in inventory_list:
            print(item)
    else:
        print('Inventory is empty.')
    print('-----------------')
    print()


main()
