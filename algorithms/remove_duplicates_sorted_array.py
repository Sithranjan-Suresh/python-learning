"""
Problem: Remove Duplicates from Sorted Array (LeetCode #26)
----------------------------------------------------------
We are given a sorted array 'nums' in non-decreasing order.
The task is to remove duplicates in-place such that each unique element 
appears only once and return the new length. The relative order of elements 
must be preserved.

Approach:
1. Use two pointers:
   - i (slow pointer) → tracks the position of the last unique element.
   - j (fast pointer) → scans through the array.
2. If nums[j] != nums[i], then we found a new unique element:
   - Increment i.
   - Place nums[j] at nums[i].
3. After the loop, i + 1 is the length of the unique array.
"""

def removeDuplicates(nums):
    # Handle empty array
    if not nums:
        return 0

    # i points to the last unique element found
    i = 0

    # j scans the array starting from index 1
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            # Found a new unique element → move i forward
            i += 1
            nums[i] = nums[j]  # Overwrite duplicate with unique element

    # Length of unique elements is i + 1
    return i + 1


# ------------------ TESTING ------------------

nums = [0,0,1,1,1,2,2,3,3,4]
length = removeDuplicates(nums)

print("Length of unique array:", length)     # Expected: 5
print("Modified array:", nums[:length])     # Expected: [0,1,2,3,4]
