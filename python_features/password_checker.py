"""
Problem: Password Strength Checker
----------------------------------
Checks if a password is strong based on the following criteria:
1. Length greater than 8 characters
2. Contains both lowercase and uppercase letters
3. Contains at least one number
4. Contains at least one special character from !@#$%^&*()-_+=
"""

# Get password input from user
password = input("Input a password: ")

# Check length
if len(password) > 8:
    print("Length is good!\n")
    
    # Check for both lowercase and uppercase letters
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        print("Contains both lower and upper case letters!\n")
        
        # Check for at least one digit
        if any(c.isdigit() for c in password):
            print("Contains a number!\n")
            
            # Check for at least one special character
            if any(c in "!@#$%^&*()-_+=" for c in password):
                print("Contains a special character!\nStrong password\n")
            else:
                print("No special characters\nWeak password\n")
        else:
            print("No numbers\nWeak password\n")
    else:
        print("Does not contain both lower and upper case letters\nWeak password\n")
else:
    print("Not enough characters\nWeak password\n")
