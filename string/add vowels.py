####program 4
#piglatin - from the input string,for each word,remove the first chars until a vowek,add it to the end of the word
#and add 'ay' to it
#answer lay maay nPython

inputSentence = "I am Python"  # Replace with your input sentence
pigLatinKey = 'ay'
vowels = ['a', 'e', 'i', 'o', 'u']

for word in inputSentence.split():  # Gets the word in a sentence
    # Take the first chars until a vowel
    first_vowel_index = 0
    
    # Check if the word has more than one character
    if len(word) > 1:
        # Iterate through the characters in the word
        for index, char in enumerate(word):
            # Check if the character is a vowel
            if char.lower() in vowels:
                first_vowel_index = index
                break  # Exit the loop once the first vowel is found
        
        # Split the word and create the Pig Latin form
        word = word[first_vowel_index:] + word[:first_vowel_index] + pigLatinKey
    else:
        # If the word has only one character, no change is made
        word = word + pigLatinKey

    print(word)









