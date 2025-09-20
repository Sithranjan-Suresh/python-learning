"""
Problem: Monthly Expenses Analysis
----------------------------------
We have a dictionary storing monthly expenses. The tasks are:
1. Calculate extra spending in February compared to January.
2. Calculate total expenses for the first quarter.
3. Check if any month had exactly 2000 dollars spent.
4. Add June’s expense to the dictionary.
"""

# Monthly expenses dictionary
expenses = {
    "January": 2200,
    "February": 2350,
    "March": 2600,
    "April": 2130,
    "May": 2190
}

# 1. Extra spending in February compared to January
print("1️⃣ In February, how many dollars did you spend extra compared to January?")
extra_feb = expenses["February"] - expenses["January"]
print(f"The answer is: ${extra_feb}\n")

# 2. Total expense in the first quarter (Jan + Feb + Mar)
print("2️⃣ Find out your total expense in the first quarter (first three months):")
first_quarter_total = expenses["January"] + expenses["February"] + expenses["March"]
print(f"The answer is: ${first_quarter_total}\n")

# 3. Check if exactly 2000 dollars was spent in any month
print("3️⃣ Did you spend exactly $2000 in any month?")
spent_2000 = any(value == 2000 for value in expenses.values())
print(f"The answer is: {'Yes' if spent_2000 else 'No'}\n")

# 4. Add June's expense
print("4️⃣ June month just finished and your expense is $1980. Adding this to the expenses list.")
expenses["June"] = 1980
print("Updated expenses:", expenses)

print("\n✅ Done!")
