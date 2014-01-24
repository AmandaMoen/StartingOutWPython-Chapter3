# Programming Exercise 3.1 Kilometer Converter
# May 3rd, 2010
# CS110
# Amanda L. Moen
# 1. Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers,
# and then converts that distance to miles.  The conversion formula
# is as follows:
#   Miles = Kilometers X 0.6214

# miles = kilometers * 0.6214

def main():
    # Ask the user for the distance in kilometers.
    kilometers = input('Enter the distance in kilometers: ')
    kilo(kilometers)
        
def kilo(kilometers):
    # Convert the kilometers to miles.
    miles = kilometers * 0.6214

    # State what the miles are.
    print 'That converts to ', miles, 'miles.'
    
# Call the main function.
main()
