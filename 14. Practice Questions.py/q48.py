"""
Q.48
write a function tax_calculation(income) that takes
annual income and returns the tax amount based on
these slabs:
* up to 2,50,000-no tax
* 2,50,000 to 5,00,000 - 5%
* 5,00,00 to 10,00,000-20%
* above 10,00,000-30%
"""
def tax_calculator(income):
    if income<250000:
        print("No tax")
    elif 250000<income<500000:
        print("5%")
    elif 500000<income<1000000:
        print("20%")
    elif income>1000000:
        print("30%")

tax_calculator(100000)
tax_calculator(450000)
tax_calculator(300000)
tax_calculator(700000)
tax_calculator(2000000)