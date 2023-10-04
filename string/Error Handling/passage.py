# From a given passage extract unique words and print them.
# Accept the passage as an input from the user
#try to incorporate error handling feature too in all the 
#above problems

while True:  #continuously prompt the user for input until valid input is provided.
    try:     #place the code that might raise an exception inside the
        passage = input("Enter the passage: ").strip() #method to remove whitespace from the input
        if passage:  # If the user provides a non-empty input
            break  #exit the while loop.
        else:
            print("Please enter a non-empty passage.")
    except KeyboardInterrupt:  #when the user interrupts the program by pressing Ctrl+C
        print("\nUser interrupted. Please enter a passage.") #a message to the user and continues to prompt for input.

# Check if the passage is empty or only whitespace
if  not passage: #variable passage is an empty string or contains only whitespace characters.
    print("The passage is empty or contains only whitespace.")
else:
    # Split the passage into words
    words = passage.split() #method to creating a list of words stored in the words variable.

    # Create a set to store unique words
    unique_words = set(words) #set automatically eliminates duplicates, so it contains only unique words

    # Print the unique words
    print("Unique words in the passage:")
    for word in unique_words: #code iterates over the unique words set
        print(word.lower()) #converts each word to lowercase using lower
