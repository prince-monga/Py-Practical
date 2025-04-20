import numpy as np

# 1. Creating NumPy arrays
arr1 = np.array([10, 20, 30, 40, 50])  # 1D array
arr2 = np.array([[11, 12], [13, 14], [15, 16]])  # 2D array

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# 2. Array properties
print("\nArray Shape (1D):", arr1.shape)
print("Array Shape (2D):", arr2.shape)
print("Array Data Type (1D):", arr1.dtype)
print("Array Data Type (2D):", arr2.dtype)

# 3. Array Operations
arr3 = np.array([5, 5, 5, 5, 5])
difference_arr = arr1 - arr3  # Element-wise subtraction
print("\nElement-wise Subtraction:", difference_arr)

# 4. Array Reshaping
reshaped_arr = arr2.reshape(2, 3)
print("\nReshaped 2D Array:\n", reshaped_arr)

# 5. Array Slicing
sliced_arr = arr2[0:2, 1]
print("\nSliced Array (First Two Rows, Column 1):", sliced_arr)

# 6. Array Broadcasting
arr4 = np.array([10, 20, 30])
arr5 = np.array([[2], [4], [6]])
broadcasted_arr = arr4 * arr5  # Broadcasting multiplies 1D array with each row of the 2D array
print("\nBroadcasting Example (Multiplication):\n", broadcasted_arr)

# 7. Array Mathematical Functions
arr6 = np.array([100, 121, 144, 169])
sqrt_arr = np.sqrt(arr6)
print("\nSquare Root of Array:", sqrt_arr)

# 8. Random Array
random_arr = np.random.randint(1, 100, size=(3, 3))  # Creating a 3x3 array with random integers between 1 and 100
print("\nRandom Integer Array:\n", random_arr)
