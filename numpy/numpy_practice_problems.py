import numpy as np
#Problem 1: Create a 1D NumPy array of numbers from 10 to 50 (inclusive), then reverse it.

arr_one = np.arange(10,51)
print(arr_one)
arr_one_reversed = arr_one[::-1]
print(arr_one_reversed)

'''Problem 2: Create a 5 x 5 array filled with random integers between 1 and 100.
Print its shape, size, and data type.
Find the min, max, and mean.'''

arr_two = np.random.randint(1,100,size=(5,5))
print(arr_two)
print(arr_two.shape)
print(arr_two.size)
print(arr_two.dtype)
print(arr_two.min())
print(arr_two.max())
print(arr_two.mean())

#Given an array of 20 random integers between 1 and 50, select only the even numbers.

arr_three = np.random.randint(1,50,size=(1,20))

even = (arr_three%2)==0
print(arr_three)
print(even)
print(arr_three[even])

#Create a 4×4 identity matrix, then add 5 to all elements in the second row only (without loops).

arr_four = np.random.randint(0, 10, size=(4, 4))
print(arr_four)
arr_four[1] = arr_four[1]+5
print(arr_four)