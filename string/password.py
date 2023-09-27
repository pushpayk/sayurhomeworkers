# Print the level of the password security and if the password is acceptable
#     Weak - only alphabets or only numbers or only special chars
#     Ok - at least one alphabet, one number and one special char
#     strong - at least three alphabets, two numbers and one special char
#     Very strong - same as strong, but at least 16 count

#     All passwords must be at least 8 chars long. You can use RegEx if you want.

import re

# Get the user's password
password = input("Enter a password: ")

number_of_alpha = len(re.findall(r'[a-zA-Z]',password))
number_of_numeric = len(re.findall(r'[0-9]',password))
number_of_splchar = len(re.findall(r'[^a-zA-Z0-9]',password))

# Check if the password is at least 8 characters long
if len(password) < 8:
    print("Weak - Password is too short. It must be at least 8 characters long.")
else:

    if number_of_alpha and number_of_numeric and number_of_splchar:
        if len(password) >= 16:
            print("Very strong - Password meets all criteria and is at least 16 characters long.")
        else:
            print("Strong - Password meets all criteria but is less than 16 characters long.")
    else:
        print("OK - Password meets minimum criteria (at least one alphabet, one number, and one special character).")

#output
#Enter a password: Pushpayk*2001
#Strong - Password meets all criteria but is less than 16 characters long.