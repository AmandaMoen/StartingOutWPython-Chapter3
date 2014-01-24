# Programming Exercise 3.5 Property Tax
# May 3rd, 2010
# CS110
# Amanda L. Moen
# 5. Property Tax
# A county collects property taxes on the assessment value of property,
# which is 60 percent of the property's actual value.  For example, if
# an acre of land is valued at $10,000, its assessment value is $6,000.
# The property tax is then $0.64 for each $100 of the assessment value.
# The tax for the acre assessed at $6,000 will be $38.40.  Write a
# program that asks for the actual value of a piece of property and
# displays the assessment value and property tax.

def main():

    # Ask for the property's actual value.
    property_value = input("Enter the property's actual value: ")
    prop(property_value)

def prop(property_value):
    # Calculate the property's assessment value
    # using the actual value.
    # assessment_value=actual_value*60%
    assessment_value = property_value * 0.6
    print 'The assessment value is $%.2f' % assessment_value
    assessment(assessment_value)

def assessment(assessment_value):
    # Calculate the property tax.
    # Property_tax=$0.64 for every $100 of assessment_value.
    property_tax = assessment_value * 0.0064
    print 'The property tax is $%.2f' % property_tax

# Call the main function.
main()
