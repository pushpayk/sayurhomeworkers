#print multiplication tables from 7 to 16, each number upto 12 rows

Tables = int(input("please enter the tables from 7 to 16:"))

for num in range(7,17): # loop from 7 to 16
    print(f"multiplication table for {num}:")
    for multipiler in range(1,13):# Loop from 1 to 12
        result = num * multipiler
        print(f"{num} * {multipiler} = {result}")   #This line prints the multiplication equation along with its result in a formatted string.
    print() # This prints an empty line after each table to separate them visually.  
