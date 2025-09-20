"""
Problem: Stranger Things Quote Guessing Game
--------------------------------------------
We want to fetch a random quote from the Stranger Things Quotes API and let 
the user guess who said it.

Approach:
1. Make an HTTP GET request to the API endpoint.
2. Parse the JSON response and extract the quote and author.
3. Display the quote and ask the user to guess who said it.
4. Compare the user’s guess with the correct author.
   - If correct → print a win message.
   - If incorrect → reveal the correct answer.
"""

import requests
import json

def get_random_quote():
    """Fetch a random Stranger Things quote from the API."""
    url = "https://strangerthings-quotes.vercel.app/api/quotes"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise error if response is not 200
        content = response.json()
        return content[0]["quote"], content[0]["author"]
    except requests.RequestException as e:
        print("Error fetching quote:", e)
        return None, None


def play_game():
    """Main game logic."""
    print("🎬 Welcome to the Stranger Things Quote Game! 🎬")

    quote, author = get_random_quote()
    if not quote or not author:
        print("Game could not start. Try again later.")
        return

    # Show the quote
    print("\nQuote:", quote)

    # Get user guess
    user_guess = input("Who said it? ")

    # Check guess
    if user_guess.strip().lower() == author.lower():
        print("Congrats, you win!")
    else:
        print(f"Wrong! The correct answer was: {author}")


# ------------------ RUN GAME ------------------
if __name__ == "__main__":
    play_game()
