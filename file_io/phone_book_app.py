"""
Problem: Phone Book Application
-------------------------------
Allows the user to:
1. Add a contact
2. View all contacts
3. Search for a contact by name
"""

# Initialize empty phone book dictionary
phoneBook = {}

while True:
    # Display options to the user
    choice = int(input('''
What do you want to do? 
1 - Add a contact
2 - View the phone book
3 - Search by name
Any other number to exit
'''))

    if choice == 1:
        # Add a new contact
        print("Okay, let's add a contact")
        name = input("What's the name? ")
        try:
            num = int(input("What's the phone number? "))
        except ValueError:
            print("Invalid phone number! Please enter digits only.")
            continue
        phoneBook[name] = num
        print(f"Contact {name} added successfully!\n")

    elif choice == 2:
        # View all contacts
        if phoneBook:
            print("\nPhone Book:")
            for name, number in phoneBook.items():
                print(f"{name}: {number}")
        else:
            print("Phone book is empty.\n")

    elif choice == 3:
        # Search for a contact
        name = input("Enter the name to search for: ")
        if name in phoneBook:
            print(f"{name}: {phoneBook[name]}\n")
        else:
            print(f"{name} not found in the phone book.\n")

    else:
        # Exit the loop
        print("Exiting the phone book application.")
        break
