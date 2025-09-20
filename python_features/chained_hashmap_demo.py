"""
Problem: Hashmap with Chaining
-------------------------------
We implement a simple hashmap using:
1. A list of buckets.
2. Each bucket stores key-value pairs in a list (chaining) to handle collisions.
3. Supports insertion, retrieval, update, and deletion.
"""

class Hashmap:
    def __init__(self):
        self.MAX = 10  # Number of buckets
        self.arr = [[] for _ in range(self.MAX)]  # Each bucket is a list
    
    def get_hash(self, key):
        """
        Compute hash for a string key using sum of character ordinals
        """
        return sum(ord(c) for c in key) % self.MAX

    def __setitem__(self, key, value):
        """
        Insert or update key-value pair
        """
        the_hash = self.get_hash(key)
        # Check if key already exists; if yes, update it
        for pair in self.arr[the_hash]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise, append new key-value pair
        self.arr[the_hash].append([key, value])

    def __getitem__(self, key):
        """
        Retrieve value for a key. Returns None if key not found.
        """
        the_hash = self.get_hash(key)
        for pair in self.arr[the_hash]:
            if pair[0] == key:
                return pair[1]
        return None

    def __delitem__(self, key):
        """
        Delete key-value pair from hashmap
        """
        the_hash = self.get_hash(key)
        for i, pair in enumerate(self.arr[the_hash]):
            if pair[0] == key:
                del self.arr[the_hash][i]
                return

# ------------------ DEMO ------------------
stock_prices = Hashmap()

# Insert stock prices
stock_prices["2025-03-01"] = 150
stock_prices["2025-03-02"] = 152
stock_prices["2025-03-03"] = 147
stock_prices["2025-03-11"] = 160  # Could collide with other keys

# Retrieve values
print(stock_prices["2025-03-01"])  # 150
print(stock_prices["2025-03-03"])  # 147
print(stock_prices["2025-03-11"])  # 160

# Update a value
stock_prices["2025-03-03"] = 149
print(stock_prices["2025-03-03"])  # 149

# Delete a value
del stock_prices["2025-03-02"]
print(stock_prices["2025-03-02"])  # None

# Collision test: Both keys in the same bucket exist
print(stock_prices["2025-03-01"])  # 150
print(stock_prices["2025-03-11"])  # 160
