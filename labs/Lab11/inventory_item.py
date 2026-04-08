#
# Caleb Hemphill
# 04/08/2026
# Inventory item class
#

CATEGORY_LIST = ['Book', 'DVD', 'Game']


class InventoryItem:
    def __init__(self, name='', count=0, cost=0.00, category=''):
        self.name = name
        self.count = count
        self.cost = cost
        self.category = category

    def get_item_input(self):
        """
        This method asks the user for the name, count, cost, and category for a particular item and assigns those
        values to the objects attributes. It validates that count, cost, and category are acceptable values and
        prompts the user if there are any issues.

        :return:
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

        # update InventoryItem attributes
        self.name = item_name
        self.count = item_count
        self.cost = unit_cost
        self.category = category

    def __str__(self):
        return f'{self.name}\n\tCount: {self.count}, Cost: {self.cost:.2f}\n\tCategory: {self.category}'
