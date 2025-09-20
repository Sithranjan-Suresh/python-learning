"""
Problem: Interactive Country Population Dictionary
--------------------------------------------------
We create a dictionary of countries and populations.
The user can:
1. Print all countries and populations.
2. Add a new country.
3. Remove an existing country.
4. Query the population of a specific country.
"""

# Initial dictionary of countries and populations (in millions)
countries = {"China": 143, "India": 136, "USA": 32, "Pakistan": 21}

# Ask user what operation they want to perform
user_input = input("What do you want to do? (print, add, remove, query): ").strip().lower()

if user_input == "print":
    # Print all countries and their populations
    print("\nCountries and Populations:")
    for country, population in countries.items():
        print(f"{country} ==> {population}")

elif user_input == "add":
    # Add a new country
    country_input = input("Enter the country to add: ").strip().capitalize()
    if country_input in countries:
        print(f"{country_input} already exists in the dictionary.")
    else:
        try:
            population = int(input(f"Enter the population for {country_input} (in millions): "))
            countries[country_input] = population
            print(f"{country_input} added successfully!")
        except ValueError:
            print("Invalid population input. Must be an integer.")

elif user_input == "remove":
    # Remove a country
    country_input = input("Enter the country to remove: ").strip().capitalize()
    if country_input in countries:
        del countries[country_input]
        print(f"{country_input} removed successfully!")
    else:
        print(f"{country_input} does not exist in the dictionary.")

    # Print updated dictionary
    print("\nUpdated Countries and Populations:")
    for country, population in countries.items():
        print(f"{country} ==> {population}")

elif user_input == "query":
    # Query a country's population
    country_input = input("Enter the country to query: ").strip().capitalize()
    if country_input in countries:
        print(f"{country_input}'s population: {countries[country_input]} million")
    else:
        print(f"{country_input} does not exist in the dictionary.")

else:
    print("Invalid input. Please enter print, add, remove, or query.")
