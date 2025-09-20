def two_sum(nums, target):
    """
    Finds two indices i, j in 'nums' such that nums[i] + nums[j] == target.
    Returns the indices as a list [i, j].
    """
    # Step 1: Create a dictionary mapping each number to its index
    num_to_index = {}
    for i, num in enumerate(nums):
        num_to_index[num] = i

    # Step 2: Check for each number if the complement exists
    for i, num in enumerate(nums):
        complement = target - num
        # Ensure we don't use the same element twice
        if complement in num_to_index and num_to_index[complement] != i:
            return [i, num_to_index[complement]]

# Example usage
print(two_sum([3, 3], 6))  # Output: [0, 1]
