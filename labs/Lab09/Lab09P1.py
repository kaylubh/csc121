#
# Caleb Hemphill
# 03/25/26
# Word counting in dictionaries
#

# DO NOT UPDATE ANY PART OF THE MAIN FUNCTION
def main():
    input_file = open('words.txt', 'r')  # Open a file for reading
    file_text = input_file.read().upper()  # Read all contents and convert to uppercase
    process_file(file_text)
    input_file.close()


def process_file(text):
    """
    This function creates a dictionary of words and their counts from the input text.
    It then identifies the words that appear the most in the dictionary, displays
    those words (with their count), and then removes them from the dictionary.
    Finally, it extracts and sorts the remaining words as a list and displays it.

    :param text: Text string to be parsed into a dictionary
    :return:
    """

    # TODO: Create an empty dictionary

    words_dictionary = {}

    # TODO: Use the split method to get a list of words from the input parameter

    words_list = text.split()

    # TODO: Use a for loop to go through the list 1-by-1
    #  and count the occurrence of each word. Add or update
    #  the entries in the dictionary with the word/count pairs.

    # add the word to the dictionary with the word as key
    # if the word is already in the dictionary increment the count by 1
    # if the key (word) is not yet in the dictionary sets the default value to 0 before incrementing
    for word in words_list:
        words_dictionary[word] = words_dictionary.get(word, 0) + 1

    # TODO: Print the dictionary

    print(words_dictionary)

    # TODO: Create a list of words with the maximum count
    #  and print the list.

    # find the max count
    max_count = max(words_dictionary.values())

    # create a list words from words_dictionary if their value matches the max count
    max_count_words = [word for word in words_dictionary.keys() if words_dictionary[word] == max_count]

    print(f'Words with max count of {max_count}: {max_count_words}')

    # TODO: Remove the words with max count from the dictionary
    #  and print the dictionary.

    # copy words dictionary
    words_dictionary_max_removed = {}
    words_dictionary_max_removed |= words_dictionary

    # remove the max count words from new dictionary
    for word in max_count_words:
        del (words_dictionary_max_removed[word])

    print(f'Dictionary with max removed: {words_dictionary_max_removed}')

    # TODO: Put all the words in the dictionary in a list, sort it,
    #  and print the list of sorted words.

    sorted_words = [word for word in words_dictionary_max_removed.keys()]
    sorted_words.sort()

    print(f'Words sorted: {sorted_words}')


main()
