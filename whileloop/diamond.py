#problem.1
#write a profram that print out the diamond shape using $.
#After printing each line,wait for the user input , if the user presses space,continue
#if the user presses any other key, stop printng. maxmum 10 line
 


rows = 5  # number of rows
i=1  #current row   #maximum no of lines to print
#to print first half of the diamond
while i <= rows :
    spaces = " " * (rows - i)
    dollar = "$" * (2 * i - 1)
    line = spaces  # spaces before the $ symbols.
    for j in range(len(dollar)):  #for loop that iterates through the characters in the dollar string
        line += dollar[j]           #adds a $ symbol to the line.
        if j < len(dollar) - 1:  # it means we are not at the last $ symbol in the line.
         line += " "    #if we are not at the last $ symbol, this line appends a space character to the line. This is how the spaces between the $ symbols are added
    print(line)
    user_input = input("")
    if user_input != " ":
        break
    i += 1

#to print the second half of the diamond
i = rows - 1
while i > 0 :
    spaces = " " * (rows - i)
    dollar = "$" * (2 * i - 1)
    line = spaces 
    for j in range(len(dollar)):
        line += dollar[j]
        if j < len(dollar) - 1:
         line += " "
    print(line)
    user_input =input ("")
    if user_input != " ":
        break
    i -=1







    

