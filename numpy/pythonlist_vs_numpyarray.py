#Proving that numpy arrays use less memory, faster, and more convinient
import numpy as np
import time
import sys

#Size of python list
l = range(1000)
print(f"Size of python list: {sys.getsizeof(4)*len(l)} bytes")

#Size of numpy array
array = np.arange(1000)
print(f"Size of numpy array: {array.size*array.itemsize} bytes")

#Initializing python lists l1 and l2
SIZE = 1000000
l1 = range(SIZE)
l2 = range(SIZE)

#Measuring speed of python lists addition
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
end = time.time()
print(f"Python list took: {(end-start)*1000} milliseconds")

#Initializing numpy arrays a1 and a2
a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

#Measuring speed of numpy arrays addition
start = time.time()
result = a1+a2
end = time.time()
print(f"numpy array took: {(end-start)*1000} milliseconds")