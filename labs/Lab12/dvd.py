#
# Caleb Hemphill
# 04/15/2026
# Inheritance and Polymorphism - Problem 1 & 2
# DVD class
#

from inventory_item import InventoryItem


class DVD(InventoryItem):
    def __init__(self, item_name='', item_count=0, unit_cost=0.00, upc='', genre=''):
        """
        This method is the class constructor. It sets the attributes of
        the class object with what is passed in by the calling routine.

        :param item_name: Name of item
        :param item_count: Number of item in inventory
        :param unit_cost: Unit cost of item
        :param upc: UPC of the DVD
        """
        super().__init__(item_name, item_count, unit_cost, "DVD")
        self.upc = upc
        self.genre = genre

    def get_item_input(self):
        """
        This method will ask the user for item data and store it
        in the class object's attributes.

        :return:
        """

        # use base class for common inputs
        super().get_item_input()

        # get UPC input
        is_valid_upc = False
        while not is_valid_upc:
            item_upc = input('What is the UPC? ')
            if item_upc.isdigit() and len(item_upc) == 12:
                is_valid_upc = True
                self.upc = item_upc
            else:
                print('UPC must be a 12 digit number.')

        # get genre input
        self.genre = input('What is the genre of the DVD? ')

    def __str__(self):
        """
        This method will return a human-readable version of the
        class object.

        :return: Human-readable string representing the object.
        """

        return (super().__str__() + '\n' +
                f'\tUPC: {self.upc}\n' +
                f'\tGenre: {self.genre}')
