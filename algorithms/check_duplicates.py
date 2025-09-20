"""
Problem: Check for duplicate numbers in a list
-----------------------------------------------
Steps:
1. Sort the list
2. Compare adjacent elements to detect duplicates
"""

# Initial list of numbers
nums = [7, 6, 3, 3, 1]

# Sort the list in ascending order
nums.sort()
print("Sorted list:", nums)

# Check for duplicates by comparing adjacent elements
for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        print(f"Duplicate found: {nums[i]}")
