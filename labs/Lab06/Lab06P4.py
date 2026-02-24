#
# Caleb Hemphill
# 02/24/2026
# matplotlib Bar Graph Generator
#

import matplotlib.pyplot as plt


def main():
    """
    Creates a matplotlib bar graph using data input from the user
    """

    # graph details input
    title = input('Enter the bar graph title: ')
    x_label = input('Enter the label for the x-axis: ')
    y_label = input('Enter the label for the y-axis: ')
    number_data_points = int(input('Enter the number of data points: '))

    # data point details input
    bar_labels = []
    bar_values = []

    for number in range(1, number_data_points + 1):
        bar_label = input(f'Enter the name for bar {number}: ')
        bar_value = float(input(f'Enter the value for bar {number}: '))
        bar_labels.append(bar_label)
        bar_values.append(bar_value)

    # create and display bar graph
    plt.bar(bar_labels, bar_values)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


if __name__ == '__main__':
    main()
