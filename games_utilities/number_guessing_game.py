"""
Problem: Number Guessing Game
-----------------------------
The program generates a random number between 1 and 100.
The user tries to guess the number.
The program gives hints (higher/lower) and counts attempts.
"""

import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)
tries = 0
user_guess = 0

# Uncomment this line to see the number for testing
# print("DEBUG: The number is", number)

print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100.")

# Game loop
while user_guess != number:
    try:
        user_guess = int(input("Enter your guess: "))
        tries += 1  # Increment tries for every valid attempt
        
        # Check if guess is in valid range
        if user_guess < 1 or user_guess > 100:
            print("The number is between 1 and 100. Try again.")
            continue
        
        # Give hints
        if user_guess > number:
            print("Guess lower!")
        elif user_guess < number:
            print("Guess higher!")
        else:
            print(f"Yay! You got it in {tries} tries!")
            break
    except ValueError:
        print("Invalid input! Please enter an integer between 1 and 100.")
