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






        

