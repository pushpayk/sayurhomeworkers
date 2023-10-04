# Get user input for start and end numbers
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# Print the header row
print("    ", end="")
for i in range(start, end + 1):
    print(f"{i:6}", end="")
print("\n  " + "#" * (6 * (end - start + 1)))

# Print the multiplication table
for i in range(start, end + 1): #i represents the row number in the multiplication table, ranging from the start to the end
    print(f"{i:3} *", end="")
    for j in range(start, end + 1): #j represents the column number in the multiplication table, also ranging from the start to the end
        print(f"{i * j:6}", end="")
    print()
