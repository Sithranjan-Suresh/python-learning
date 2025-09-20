"""
Problem: Remote Control Iterator
--------------------------------
Create a class that iterates through TV channels using Python's iterator protocol.
"""

class RemoteControl:
    def __init__(self):
        # List of channels
        self.channels = ["HBO", "CNN", "ABC", "ESPN"]
        # Index to keep track of current channel
        self.index = -1

    def __iter__(self):
        """
        Returns the iterator object itself
        """
        return self

    def __next__(self):
        """
        Returns the next channel in the list
        Raises StopIteration when all channels have been iterated
        """
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

# ------------------ DEMO ------------------
r = RemoteControl()
itr = iter(r)

# Iterate manually using next()
try:
    print(next(itr))  # HBO
    print(next(itr))  # CNN
    print(next(itr))  # ABC
    print(next(itr))  # ESPN
    print(next(itr))  # Raises StopIteration
except StopIteration:
    print("No more channels!")
