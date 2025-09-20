"""
Problem: Python Comprehensions and Zip Usage
--------------------------------------------
We demonstrate:
1. List comprehensions for filtering and transforming data.
2. Zipping two lists together.
3. Dictionary comprehension to create a mapping.
"""

# 1️⃣ List comprehension to get even numbers from 1 to 9
even_numbers = [i for i in range(1, 10) if i % 2 == 0]
print("Even numbers:", even_numbers)

# 2️⃣ List comprehension to get squares of numbers from 1 to 9
squares = [i**2 for i in range(1, 10)]
print("Squares:", squares)

# 3️⃣ Zip two lists (cities and countries) and print pairs
cities = ["a", "b", "c"]
countries = ["x", "y", "z"]
zipped_pairs = zip(cities, countries)

print("City-Country pairs:")
for city, country in zipped_pairs:
    print((city, country))

# 4️⃣ Dictionary comprehension using zip
city_country_dict = {city: country for city, country in zip(cities, countries)}
print("City-Country dictionary:", city_country_dict)
