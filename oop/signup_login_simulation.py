"""
Problem: Simple Signup/Login Simulation
---------------------------------------
We want to create a basic program that allows users to:
1. Sign up with a username and password.
2. Log in with their credentials.
3. Greet the user upon successful login or signup.
"""

# Dictionary to store username:password pairs
database = {}

while True:
    # Ask user to signup or login
    choice = input("Do you want to signup or login? Type 'signup', 'login', or 'exit': ").strip().lower()

    if choice == "signup":
        # Get user details for signup
        username = input("What's your username? ").strip()
        password = input("What's your password? ").strip()

        if username in database:
            print("Username already exists! Try logging in.")
        else:
            database[username] = password
            print("✅ You're signed up successfully!")

    elif choice == "login":
        # Get user details for login
        username = input("What's your username? ").strip()
        password = input("What's your password? ").strip()

        # Check if username exists
        if username in database:
            if database[username] == password:
                print("✅ You're logged in successfully!")
            else:
                print("❌ Incorrect password. Try again.")
        else:
            print("❌ Username does not exist. Please signup first.")

    elif choice == "exit":
        print("👋 Exiting the program. Goodbye!")
        break

    else:
        print("❌ Invalid input. Please type 'signup', 'login', or 'exit'.")

    # Greet the user if login or signup was successful
    if choice in ["signup", "login"] and username in database and database[username] == password:
        print(f"Hello {username}! Welcome to the dashboard.\n")
