"""
Problem: Simulating a Remote Control with Generators
----------------------------------------------------
We use a generator to simulate changing TV channels.
1. `remote_control_next()` yields channels one by one.
2. Iterate over the generator to "switch" channels.
"""

# Generator function for TV channels
def remote_control_next():
    yield "CNN"
    yield "ESPN"
    yield "ABC"

# ------------------ DEMO ------------------
# Get the generator iterator
channels = remote_control_next()

# Iterate through the channels
for channel in channels:
    print("Now watching:", channel)
