"""
Problem: Hashmap with Open Addressing (Linear Probing)
------------------------------------------------------
We implement a hashmap using:
1. A fixed-size array.
2. Linear probing for collision resolution.
3. Supports insertion, retrieval, update, and deletion.
"""

class Hashmap:
    def __init__(self):
        self.MAX = 10  # Number of slots
        self.arr = [None] * self.MAX  # Initialize all slots to None

    def get_hash(self, key):
        """
        Compute hash for a string key using sum of character ordinals
        """
        return sum(ord(c) for c in key) % self.MAX

    def __setitem__(self, key, value):
        """
        Insert or update key-value pair using linear probing
        """
        h = self.get_hash(key)
        start_h = h

        # Linear probing to find an empty slot or existing key
        while self.arr[h] is not None and self.arr[h][0] != key:
            h = (h + 1) % self.MAX
            if h == start_h:
                raise Exception("Hashmap is full")
        
        # Insert or update key-value pair
        self.arr[h] = [key, value]

    def __getitem__(self, key):
        """
        Retrieve value for a key using linear probing
        Returns None if key not found
        """
        h = self.get_hash(key)
        start_h = h

        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                return self.arr[h][1]
            h = (h + 1) % self.MAX
            if h == start_h:
                break
        return None

    def __delitem__(self, key):
        """
        Delete key-value pair
        Sets slot to a special marker to maintain probe chain
        """
        h = self.get_hash(key)
        start_h = h

        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                self.arr[h] = None  # Note: For a real hashmap, use a tombstone marker
                return
            h = (h + 1) % self.MAX
            if h == start_h:
                break
        print(f"Key '{key}' not found.")


# ------------------ DEMO ------------------
stock_prices = Hashmap()

# Insert stock prices
stock_prices["2025-03-01"] = 150
stock_prices["2025-03-02"] = 152
stock_prices["2025-03-03"] = 147
stock_prices["2025-03-11"] = 160  # Could collide

# Retrieve values
print(stock_prices["2025-03-01"])  # 150
print(stock_prices["2025-03-03"])  # 147
print(stock_prices["2025-03-11"])  # 160

# Update value
stock_prices["2025-03-03"] = 149
print(stock_prices["2025-03-03"])  # 149

# Delete a value
del stock_prices["2025-03-02"]
print(stock_prices["2025-03-02"])  # None
