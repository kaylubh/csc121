#
# Caleb Hemphill
# 04/01/2026
# Starter Code for Lab 10 Problem 2 (Remove this line before submitting)
# Trish's Bookstore Inventory System
#

import pickle

CATEGORY_LIST = ['Book', 'DVD', 'Game']


# Review the main() function and update TODO sections.
# Do not change any other code within main().
def main():
    inventory_counts, inventory_costs, inventory_categories = read_inventory_file()

    print("Welcome to Trish's Inventory Input System")
    print("Current Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_categories)

    response = ''
    while response != '0':
        display_menu()
        response = input('Enter your choice: ')

        if response == "1":  # Add an item
            item_name, item_count, unit_cost, category = get_item_input()
            # DONE - Replace pass with code that will add the item_name,
            #  item_count, and unit_cost data to the dictionaries

            # updates inventory count or starts a new count if it is a new item
            inventory_counts[item_name] = inventory_counts.get(item_name, 0) + item_count
            # adds or updates the cost and category for the item
            inventory_costs[item_name] = unit_cost
            inventory_categories[item_name] = category

        elif response == "2":  # Display a single item
            print()
            item_name = input('Enter item name: ')
            # DONE - Replace pass with code that will display the item data
            #  from the dictionaries or display "Not found"

            if item_name not in inventory_counts:
                print(f'{item_name}: Not Found')
            else:
                print(item_name)
                print(f'\tCount: {inventory_counts[item_name]}, Cost: {inventory_costs[item_name]:.2f}')
                print(f'\tCategory: {inventory_categories[item_name]}')

        elif response == "3":  # Display items in a category
            print()
            category_name = input('Enter category name: ')
            print(f'\nItems in {category_name}:')
            if category_name in CATEGORY_LIST:
                # DONE - Replace pass with code that will print the names
                #  of all the items in the category

                for key, value in inventory_categories.items():
                    if value == category_name:
                        print(f'\t{key}')
            else:
                print(f'{category_name} not in list of categories: {CATEGORY_LIST}')

        elif response == "4":  # Delete a single item
            print()
            item_name = input('Enter item name: ')
            # DONE - Replace pass with code that will remove the item data
            #  from the dictionaries or display "Not found"

            if item_name not in inventory_counts:
                print(f'{item_name}: Not Found')
            else:
                del inventory_counts[item_name]
                del inventory_costs[item_name]
                del inventory_categories[item_name]
                print(f'{item_name} deleted.')

        elif response == "5":  # Display all inventory
            # DONE - Replace pass with code that will display all the inventory
            #  items - HINT Don't we already have a function that does that?

            display_all_inventory(inventory_counts, inventory_costs, inventory_categories)

        elif response != "0":
            print("Invalid choice. Try again.\n")

        print()

    # Ready to exit the program, display and save inventory as last steps
    print("Final Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_categories)
    save_inventory_file(inventory_counts, inventory_costs, inventory_categories)


def display_menu():
    """
    This function displays a menu of options for the user.

    :return:
    """
    print("What would you like to do?")
    print("(1) Add an item\n"
          "(2) Display an item\n"
          "(3) Display a category\n"
          "(4) Delete an item\n"
          "(5) Display all inventory\n"
          "(0) Exit")


def display_all_inventory(inventory_counts, inventory_costs, inventory_categories):
    """
    This function displays all of the inventory items. If there is no
    inventory, the function displays "== Empty ==". Note that all the
    dictionaries should have the same keys which represent the item
    names.

    :param inventory_counts: Dictionary of item counts
    :param inventory_costs: Dictionary of item costs
    :param inventory_categories: Dictionary of item categories.
    :return:
    """

    # TODO - Replace pass with code that will iterate through the dictionaries
    #  that are passed in and display the inventory. If the dictionaries are
    #  empty the display "== Empty =="

    if inventory_counts:
        # headers
        print(f"{'Item Name':14}  {'Count':5}  {'Unit Cost':9}  {'Category':20}")
        print(f"{'---------':14}  {'-----':5}  {'---------':9}  {'--------':20}")
        # items
        
    else:
        print('== Empty ==')

    print()


def save_inventory_file(inventory_counts, inventory_costs, inventory_categories):
    """
    This function saves the 3 input dictionaries in a binary file named
    inventory.dat.

    :param inventory_counts: Dictionary of item counts
    :param inventory_costs: Dictionary of item costs
    :param inventory_categories: Dictionary of item categories.
    :return:
    """

    # DONE - Replace pass with code that will save your dictionaries to
    #  inventory.dat using the pickle module.

    inventory_file = open('inventory.dat', 'wb')
    pickle.dump(inventory_counts, inventory_file)
    pickle.dump(inventory_costs, inventory_file)
    pickle.dump(inventory_categories, inventory_file)
    inventory_file.close()

    print(f'\nInventory saved to inventory.dat.')


def read_inventory_file():
    """
    This function reads in 3 dictionaries from a binary file named
    inventory.dat and returns those dictionaries to the calling
    routine. If the file does not exist, it returns 3 empty dictionaries.

    :return: Current inventory in 3 dictionaries.
    """

    inventory_counts = {}
    inventory_costs = {}
    inventory_categories = {}
    # DONE - Replace pass with code that will read your dictionaries from
    #  inventory.dat using the pickle module.

    try:
        inventory_file = open('inventory.dat', 'rb')
        inventory_counts = pickle.load(inventory_file)
        inventory_costs = pickle.load(inventory_file)
        inventory_categories = pickle.load(inventory_file)
        inventory_file.close()
    except FileNotFoundError:
        pass

    return inventory_counts, inventory_costs, inventory_categories


# This function is complete, no changes needed, but feel free to review
def get_item_input():
    """
    This function asks the user for the name, count, cost, and category
    for a particular item and returns those values to the calling
    routine. It validates that count, cost, and category are acceptable
    values and prompts the user if there are any issues.

    :return: Name, count, cost, and category entered by user (validated)
    """

    # Get item name
    item_name = input('Enter the item name: ')
    # Get item count
    while True:
        try:
            item_count = int(input('Enter the item count: '))
            if item_count < 0:
                print('Item count must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Item count must be an integer.')
    # Get unit cost
    while True:
        try:
            unit_cost = float(input('Enter the unit cost: '))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Unit cost must be an integer.')
    # Get category
    while True:
        category = input('Enter the category: ')
        if category not in CATEGORY_LIST:
            print(f'Category must be in this list: {CATEGORY_LIST}')
        else:
            break
    return item_name, item_count, unit_cost, category


main()
