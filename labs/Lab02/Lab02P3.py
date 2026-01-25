#
# Caleb Hemphill
# 01/25/2026
# Sample store program to determine eligibility for a gift card loyalty program based on purchase amount
# Uses input total purchase amount to output sales tax, combined total, and gift card amount
#

# input purchase amount and loyalty status
purchase_amount = float(input('Enter the total purchase amount: '))
loyalty_status = input('Is the customer a loyalty program member (y/n): ')

# calculate total
SALES_TAX_RATE = 0.065
sales_tax = purchase_amount * SALES_TAX_RATE
total  = sales_tax + purchase_amount

# determine gift card eligibility and amount
gift_card_amount = 0
if loyalty_status == 'y':
    if purchase_amount > 50 and purchase_amount <= 100:
        gift_card_amount = 15
    elif purchase_amount > 100 :
        gift_card_amount = 25
elif loyalty_status == 'n' and purchase_amount > 100:
    gift_card_amount = 5

# output totals and gift card information
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total After Tax: ${total:.2f}')
print(f'Gift Card Awarded: ${gift_card_amount}')