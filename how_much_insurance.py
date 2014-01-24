# Programming Exercise 3.3 How Much Insurance?
# May 3rd, 2010
# CS110
# Amanda L. Moen
# 3. How Much Insurance?
# Many financial experts advise that property owners should insure
# their homes or buildings for at least 80 percent of the amount
# it would cost to replace the structure.  Write a program that
# asks the user to enter the replacement cost of a building and
# then displays the minimum amount of insurance he or she should
# buy for the property.

def main():
    # Ask for the replacement cost of the insured building.
    replacement_cost = input('Enter the replacement cost of the building: ')
    replace(replacement_cost)

def replace(replacement_cost):
    # Find what 80% of the value is.
    insurance_value = replacement_cost * 0.8

    # State what the minimum insurance needed is.
    print 'The minimum amount of insurance you need is $%.2f' % insurance_value, ' dollars.'


# Call the main function.
main()
