########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputSentence = " Beauty is a light in the heart"  #  sentence
pigLatinKey = 'ay' #common suffix added to Pig Latin 
for word in inputSentence.split():  # gets the word in a sentence
    # Take the first char
    firstChar = word[0]
    
    # Check if the word has more than one char
    if len(word) > 1:
         word = word[1:] + firstChar + pigLatinKey
    else:
        word = firstChar + pigLatinKey
    
    print(word)




