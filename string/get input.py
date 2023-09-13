###program1 ###
#get an input string from the user. add space at every 3rd char.
 
inputString = input("Enter the string :")
i=0 #counter to track chars
newString = " "   #to store the modified string. newString is initially set to an empty space.
while i < len(inputString) :
    newString += inputString[i:i+2]  #this line takes a slice of inputString from the current index i to i + 2, effectively extracting two characters at a time.
    newString += " " #add space
    i+=2    # Move to the next pair of characters

#check to add the chars at the end
if i != len(inputString) - 1 :   #checks if there are any remaining characters at the end of inputString
        newString += inputString[i:] #extracts a portion of inputString from the specified index i to the end and adds it to the newString
print("New String :",newString)
