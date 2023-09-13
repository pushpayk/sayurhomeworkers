########## Program 2
#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM

myName = "Pushpa"  #will be the name that is printed in the pyramid

for letter in myName: # iterates over each letter in the myName string. It essentially goes through the name letter by letter.
    print(myName[:myName.index(letter) + 1])  # It extracts a substring of myName from the beginning  of index 0 and including the current 