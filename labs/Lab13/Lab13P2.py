# Caleb Hemphill
# 04/22/2026
# Determine if a given string is a palindrome
# (identical forwards and backwards)
#

def palindrome(text):
    """
    Remove punctuation, spaces, convert into lowercase, then check if string is palindrome
    :param text: string value to check
    :return: boolean if text is a palindrome
    """
    text = remove_punctuation(remove_spaces(text.lower()))
    if len(text) <= 1:
        return True
    else:
        return text[0] == text[-1] and palindrome(text[1:-1])


def remove_spaces(text):
    """
    remove whitespace from a string value
    :param text: string value
    :return: text without whitespace
    """
    text = text.replace(' ', '')
    return text


def remove_punctuation(text):
    """
    Ignore the following punctuation:
    commas, hyphens, single-quotes, double-quotes, periods, and exclamation points
    :param text: text with punctuation
    :return: text without punctuation
    """
    for char in ",-'\".!":
        text = text.replace(char, '')
    return text


def main():
    result = True
    while result:
        text = input('Enter a string: ')
        result = palindrome(text)
        output = "IS" if result else "IS NOT"
        print(f' "{text}" {output} a palindrome')


if __name__ == '__main__':
    main()

# Palindromes
# level
# 1234321
# Race car
# a man, a plan, a canal, Panama!
# no lemon, no melon
# never even
# ()[42]]24[)(
# Madam, I'm Adam

# Not palindromes
# 12345
# abracadabra
# seven-eleven
# never even or odd
