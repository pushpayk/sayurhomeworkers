monthlySalesList = [5, 23, 21, 14, 23, 12, 4, 12, 22, 22, 34, 12]

# Initialize variables
basePay = 10000
bonusFor5Phones = 5000
bonusPerPhoneAfter5 = 1100
additionalBonus = 5000
previousMonthSalary = 0
cumulativeBonus = 0 #keeps track of the cumulative bonus earned over multiple months.

for month, phoneCount in enumerate(monthlySalesList):
    # Calculate the bonus for the month
    if phoneCount >= 5:
        bonus = bonusFor5Phones + (phoneCount - 5) * bonusPerPhoneAfter5
    else:
        bonus = 0

    # Calculate the current month's salary
    currentMonthSalary = basePay + bonus

    # Check for the cumulative bonus condition
    cumulativeBonus += bonus
    if cumulativeBonus >= 100000:
        basePay *= 1.05  # Increase base salary by 5%

    # Check for the additional bonus condition
    if previousMonthSalary > 20000 and phoneCount >= 20:
        currentMonthSalary += additionalBonus

    print(f"This month's salary before additional bonus: {currentMonthSalary}")

    previousMonthSalary = currentMonthSalary
#This code calculates the salary for each month, tracks the cumulative bonus, and increases the base salary by 5% if the cumulative bonus exceeds one lakh. It also checks for the additional bonus condition based on the previous month's salary and phone sales.

