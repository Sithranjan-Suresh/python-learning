"""
Problem: Search Algorithms
--------------------------
We implement two common search algorithms:
1. Linear Search - scan through each element sequentially.
2. Binary Search - divide and conquer approach on a sorted list.

Functions:
- linear_search(array, num) -> returns index of num or -1 if not found
- binary_search(array, num) -> returns index of num or -1 if not found
"""

def linear_search(array, num):
    """
    Linear search algorithm:
    1. Traverse the list from start to end.
    2. If the target number is found, return its index.
    3. If the number is not found, return -1.
    """
    for i in range(len(array)):
        if array[i] == num:
            return i
    return -1  # Number not found


def binary_search(array, num):
    """
    Binary search algorithm (requires sorted list):
    1. Initialize low and high pointers.
    2. Calculate mid index and compare with target number.
    3. If mid element is target, return index.
    4. If target < mid element, move high pointer left.
    5. If target > mid element, move low pointer right.
    6. Repeat until low > high. Return -1 if not found.
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == num:
            return mid
        elif num < array[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # Number not found


# ------------------ TESTING ------------------
if __name__ == '__main__':
    print("🔍 Search Algorithms Demo")

    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]  # Must be sorted for binary search
    number_to_find = 45

    # Linear search test
    index_linear = linear_search(numbers_list, number_to_find)
    print(f"Linear Search: Number {number_to_find} found at index {index_linear}")

    # Binary search test
    index_binary = binary_search(numbers_list, number_to_find)
    print(f"Binary Search: Number {number_to_find} found at index {index_binary}")
