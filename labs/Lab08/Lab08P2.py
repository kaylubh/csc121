#
# Caleb Hemphill
# 03/15/2026
# Sales report items category totals
#

def main():
    """
    Reads a sales file called 'sales.txt' located in the current directory and totals the sales for each category of
    items: books, DVDs, and games. Creates a sales report file named 'daily_report.txt' with the totals. Displays any
    errors in the console.
    """
    books_total = 0
    dvds_total = 0
    games_total = 0

    # open sales file and handle missing file error
    try:
        sales_file = open('sales.txt', 'r')
    except FileNotFoundError:
        print("File 'sales.txt' not found")
        return

    # total each category of sales
    line_number = 0  # keep track of line number for errors

    for line in sales_file:
        # extract category and price, remove spaces
        line_parts = line.split(',')
        category = line_parts[1].strip()
        price = line_parts[2].strip()

        # handle and display price format errors
        try:
            line_number += 1
            price = float(price)
        except ValueError:
            print(f'Error on line {line_number}: Could not convert "{price}" to price format')
            continue

        if category == 'Book':
            books_total += price
        elif category == 'DVD':
            dvds_total += price
        elif category == 'Game':
            games_total += price

    sales_file.close()

    # generate sales report
    sales_report = open('daily_report.txt', 'w')

    sales_report.write(f'Books: {books_total:.2f}\n')
    sales_report.write(f'DVDs: {dvds_total:.2f}\n')
    sales_report.write(f'Games: {games_total:.2f}\n')

    sales_report.close()


main()
