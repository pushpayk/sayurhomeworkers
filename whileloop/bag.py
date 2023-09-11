########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold

# Initialize variables
redBags, whiteBags = 100, 200
totalSales, totalBagsSold = 0, 0

while totalSales < 10000 and totalBagsSold < 10:

# Ask the customer for input
    bagsToBuy = int(input("How many bags do you want to buy? "))
    redBags = int(input(" In the above mentioned how many red bags you want ,Red bags - Rs 1000 each"))
    whiteBags = int(input(" how many white bags you want to buy,White bags - Rs 1500 each "))

    # Calculate the total cost for the bags
    if bagsToBuy <= redBags:
        redCost = bagsToBuy * 1000
        whiteCost = 0
    else:
        redCost = redBags * 1000
        whiteCost = (bagsToBuy - redBags) * 1500

    totalCost = redCost + whiteCost
# Increment the number of bags sold and update total sales
    totalBagsSold += bagsToBuy
    totalSales += totalCost

    # Display the total sales and total number of bags sold
print("Total Sales:", totalSales)
print("Total Bags Sold:", totalBagsSold)