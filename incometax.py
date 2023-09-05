income = int(input("Please enter your annual income: "))

salaries = [250000,300000, 500000, 650000, 1000000, 1500000]
tax_percentage = [0,0.05, 0.10, 0.15, 0.20, 0.30]

# Initialize tax and the previous salary
tax = 0
prev_salary = 0

for i in range(len(salaries)):
    if income <= prev_salary:
        break
    
    if income <= salaries[i]:
        taxable_income = income - prev_salary
    else:
        taxable_income = salaries[i] - prev_salary
    
    tax += taxable_income * tax_percentage[i]
    prev_salary = salaries[i]

print(f"Your income tax is: {tax}")






        


# if income <= 300000:  #3 Lakh nill
#     tax = 0
# elif income <= 500000: #5 Lakh 5% tax
#     tax = (income - 3000000) * 0.05
# elif income <= 650000: #6 lakh 50 thousand 10% tax
#     tax = (income - 500000) * 0.10 + 12500 
# elif income <= 1000000: #10 Lakh 15% tax
#     tax = (income - 600000) * 0.15 + 37500 
# elif income <= 1150000: #11 lakh 50 thousand 20% tax
#     tax = (income - 1000000) * 0.20 + 75000 
# elif income <= 1500000: #15 lakh 25%
#     tax = (income - 1250000) * 0.25 + 125000 
# else:
#     tax = (income - 1500000) * 0.30 + 187500
# print("your Income", tax, "Rupees in tax!")