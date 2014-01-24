# Programming Exercise 3.9 Paint Job Estimator
# May 3rd, 2010
# CS110
# Amanda L. Moen
# 9. Paint Job Estimator
# A painting company has determined that for every 115 square feet
# of wall space, one gallon of paint and eight hours of labor will
# be required.  The company charges $20.00 per hour for labor.
# Write a program that asks the user to enter the square feet of
# wall space to be painted and the price of the paint per gallon.
# The program should display the following data:
#   The number of gallons of paint required
#   The hours of labor required
#   The cost of the paint
#   The labor charges
#   The total cost of the paint job

def main():

    # Ask for the square footage of wall space to be painted.
    square_footage = input('Enter the number of square feet to be painted: ')
    
    # Ask for the price of the paint per gallon.
    price_gallon = input('Enter the price of the paint per gallon: ')

    estimate(square_footage, price_gallon)

def estimate(square_footage, price_gallon):
    # 115 sq ft = 1 gallon + 8 hrs of labor (labor is $20 per hour)
    num_gallons = square_footage/115
    hours_labor = num_gallons * 8
    total_price_gallon = num_gallons * price_gallon
    total_labor = hours_labor * 20
    final_total = total_price_gallon + total_labor
    print 'The total estimated price for this paint job is $', final_total

# Call the main function.
main()
