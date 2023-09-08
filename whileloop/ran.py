#computer will guess a random number.
# user has to guess that number, for each guess, print 'high'
# or 'low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# get user input and print 'high' or 'low

import random

computerNo = random.randint(3, 9)
attempt = 0

while True:
    userNo = int(input("Please guess the number between 3 and 9: "))

    if userNo == computerNo:
        print("You are right!")
        break
    elif userNo > computerNo:
        print("Too high")
    elif userNo < computerNo:
        print("Too low")
    
    attempt += 1

    print("User guessed the number in", attempt, "attempts")