#
# Caleb Hemphill
# 03/03/2026
# IP address validator
#

def main():
    input_address = input("Please enter an IP address or 'Q' to quit: ")

    while input_address.upper() != 'Q':
        address_parts = input_address.split('.')

        if len(address_parts) != 4:
            print('Error: An IP address should consist of 4 parts separated by periods.')
        else:
            error_flag = False
            for part in address_parts:
                if not part.isdigit() or not (0 <= int(part) <= 255):
                    print('Each part of the IP address should be a number between 0 and 255.')
                    error_flag = True
                    break
            if error_flag == False:
                formatted_address = input_address.replace('.', ':')
                print(f'Reformatted IP address: {formatted_address}')

        input_address = input("Please enter an IP address or 'Q' to quit: ")


main()
