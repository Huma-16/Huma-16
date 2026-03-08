import numpy as np
import time
# 1D Array
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:\n", arr1)

# 2D Array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print("\n2D Array:\n", arr2)

# Zeros and Ones
zeros = np.zeros((3,3))
ones = np.ones((2,4))
print("\nZeros:\n", zeros)
print("\nOnes:\n", ones)

# Random Array
random_arr = np.random.rand(3,3)
print("\nRandom Array:\n", random_arr)


print("\nFirst element:", arr1[0])
print("Last element:", arr1[-1])

print("\nFirst row of arr2:", arr2[0])
print("Second column of arr2:", arr2[:,1])

print("\nSlice arr1 (index 1 to 3):", arr1[1:4])

print("\nAddition:", arr1 + 5)
print("Multiplication:", arr1 * 2)
print("Square:", arr1 ** 2)

print ("\nAddition:", arr2 + 10)
print ("\nSubtraction:", arr2 - 2)
print ("\nDivided:", arr2/2)
print("\nCube:", arr2 ** 3)

print("\nSum of arr2:", np.sum(arr2))
print("Sum column-wise:", np.sum(arr2, axis=0))
print("Sum row-wise:", np.sum(arr2, axis=1))

print("\nMean:", np.mean(arr2))
print("Max:", np.max(arr2))
print("Min:", np.min(arr2))
print("Standard Deviation:", np.std(arr2))


# Reshaping
reshaped = arr1.reshape(5,1)
print("\nReshaped Array:\n", reshaped)

# Broadcasting
broadcast_result = arr2 + 10
print("\nBroadcasting Result:\n", broadcast_result)

# Save array
np.save("my_array.npy", arr2)

# Load array
loaded_array = np.load("my_array.npy")
print("\nLoaded Array:\n", loaded_array)

project1_numpy_data_explorer.py