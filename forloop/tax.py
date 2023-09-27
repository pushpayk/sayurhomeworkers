income = int(input("Please enter your annual income: "))
salaries =[250000,500000,750000,1000000,1250000,1500000]  #income thresholds for different tax brackets.
tax_percentage =[0 ,0.05,0.10,0.15,0.20,0.25]   # contains the tax rates for each tax bracket as a decimal 
previous_tax = [0,12500,37500 ,75000,125000]    #contains the cumulative tax paid up to the previous tax bracket.

#Check if the income is less than or equal to the first bracket
if income <= salaries[0]: 
    tax = 0

else:
    # Iterate through the tax brackets
    for i in range(1, len(salaries)):
        if income <= salaries[i]:
            # Calculate tax based on the current bracket
            tax = (income - salaries[i - 1]) * tax_percentage[i] + previous_tax[i - 1]
            break   # is used to exit the loop once the income is found to be within a tax bracket.
    else:
        # If income is above the highest bracket, calculate tax for the highest bracket
        tax = (income - salaries[-1]) * tax_percentage[-1] + previous_tax[-1]

print("Your income tax is: Rs.", tax)


