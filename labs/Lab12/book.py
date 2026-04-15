#
# Caleb Hemphill
# 04/15/2026
# Inheritance and Polymorphism - Problem 1 & 2
# Book class
#

from inventory_item import InventoryItem


class Book(InventoryItem):
    def __init__(self, item_name='', item_count=0, unit_cost=0.00, isbn13=''):
        """
        This method is the class constructor. It sets the attributes of
        the class object with what is passed in by the calling routine.

        :param item_name: Name of item
        :param item_count: Number of item in inventory
        :param unit_cost: Unit cost of item
        :param isbn13: ISBN of the book
        """
        super().__init__(item_name, item_count, unit_cost, "Book")
        self.isbn13 = isbn13

    def get_item_input(self):
        """
        This method will ask the user for item data and store it
        in the class object's attributes.

        :return:
        """
        # DONE - Call the base class get_item_input() using
        # the super() function.

        super().get_item_input()

        # DONE - Ask the user for the isbn13. Validate that
        # it is all digits and has 13 characters

        is_valid_isbn = False
        while not is_valid_isbn:
            item_isbn13 = input('What is the ISBN? ')
            if item_isbn13.isdigit() and len(item_isbn13) == 13:
                is_valid_isbn = True
                self.isbn13 = item_isbn13
            else:
                print('ISBN must be a 13 digit number.')

    def __str__(self):
        """
        This method will return a human-readable version of the
        class object.

        :return: Human-readable string representing the object.
        """

        return (super().__str__() + '\n' +
                f'\tISBN: {self.isbn13}')
