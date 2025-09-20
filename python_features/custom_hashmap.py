"""
Problem: Custom HashMap Implementation
--------------------------------------
We implement a simple hashmap in Python using lists.
1. Handles basic operations: set, get, delete.
2. Uses a simple hash function based on character codes.
3. Handles collisions using chaining (list of key-value pairs in each bucket).
"""

class Hashmap:
    def __init__(self):
        self.MAX = 10  # Number of buckets
        self.arr = [[] for _ in range(self.MAX)]  # Each bucket is a list (chaining)
    
    def get_hash(self, key):
        """
        Compute hash for a string key
        """
        return sum(ord(c) for c in key) % self.MAX
    
    def __setitem__(self, key, value):
        """
        Set key-value pair in the hashmap
        Handles collisions by chaining
        """
        h = self.get_hash(key)
        # Check if key exists and update
        for idx, (k, v) in enumerate(self.arr[h]):
            if k == key:
                self.arr[h][idx] = (key, value)
                return
        # Otherwise, append new key-value pair
        self.arr[h].append((key, value))
    
    def __getitem__(self, key):
        """
        Retrieve value for a given key
        """
        h = self.get_hash(key)
        for k, v in self.arr[h]:
            if k == key:
                return v
        return None  # Key not found
    
    def __delitem__(self, key):
        """
        Delete key-value pair from hashmap
        """
        h = self.get_hash(key)
        for idx, (k, v) in enumerate(self.arr[h]):
            if k == key:
                del self.arr[h][idx]
                return
        print(f"Key '{key}' not found.")

# ------------------ DEMO ------------------
hello = Hashmap()
hello["march 6"] = 130
hello["march 17"] = 21

print("Hash for 'march 6':", hello.get_hash("march 6"))
print("Hash for 'march 17':", hello.get_hash("march 17"))

print("Value for 'march 6':", hello["march 6"])
print("Value for 'march 17':", hello["march 17"])

del hello["march 6"]
print("After deletion, value for 'march 6':", hello["march 6"])
