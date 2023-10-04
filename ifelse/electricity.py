#electricity bill


def calculate_bill(units):
    if units == 0:
       print(" entry a valid number")
    elif units <= 50:
        cost = units * 0.5
    elif units <= 100:
        cost = 50 * 0.5 + (units - 50) * 0.75
    elif units <= 200:
        cost = 50 * 0.5 + 50 * 0.75 + (units - 100) * 1.2
    else:
        cost = 50 * 0.5 + 50 * 0.75 + 100 * 1.2 + (units - 200) * 1.5
    return cost  


# Create an empty list to store units consumed
unit_list = []

# Input the number of customers
num_customers = int(input("Enter the number of customers: "))

# Input units consumed for each customer and store in the list
for i in range(num_customers):
    units = float(input(f"Enter the units consumed for customer {i + 1}: "))
    unit_list.append(units)

# Display the stored units
print("Units consumed for each customer:", unit_list)

print("\nElectricity Bill\n")
print("Customer\tUnits\tCost")
print("==============================")

total_cost = 0

for i in range(num_customers): # 
     cost = calculate_bill(unit_list[i])
     total_cost += cost 
     print(f"  {i + 1}\t\t  {unit_list[i]}\t  {cost:.2f}")
 
print(f"Total Cost: {total_cost:.2f}")

