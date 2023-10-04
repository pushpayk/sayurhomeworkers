# Check if the username and password is correct. 
#      Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
#      passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
#      name of the company mentioned in the username, followed by any 3 numbers.
#      eg username : myname@sayur.com. password - mnamesay123

import re

# Input username and password for validation
username = input("Enter username: ")
password = input("Enter password: ")



# Check if the username and password meet the specified criteria
if '@' in username and (username.endswith('.com') or username.endswith('.edu') or username.endswith('.tech') or username.endswith('.org')):
        # Extract the company name from the username
        company_name = username.split('@')[1].split('.')[0]

       # Extract any 3 digits from the username
        digits = ''.join(filter(str.isdigit, username))[-3:]
        # Generate the expected password
        expected_password = f"{username[:3]}{username[2]}{digits}{company_name[:3]}"
    
        # Check if the provided password matches the expected password
        if password == expected_password:
            print("Username and password are correct.")
        else:
            print("Password is incorrect.")
else:
    print("Username is invalid or domain is not allowed.")






    



