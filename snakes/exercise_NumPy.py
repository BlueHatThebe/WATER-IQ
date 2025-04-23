import numpy as np

# 1. Array Creation
print("1. Array Creation")
a = np.array([1, 2, 3, 4, 5])  # 1D array
b = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
zeros = np.zeros((2, 3))  # Array of zeros
ones = np.ones((3, 2))  # Array of ones
arange = np.arange(0, 10, 2)  # Array with range
linspace = np.linspace(0, 1, 5)  # Linearly spaced array

print("1D array:", a)
print("2D array:\n", b)
print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Arange:", arange)
print("Linspace:", linspace)

# 2. Array Operations
print("\n2. Array Operations")
c = a + 2  # Element-wise addition
d = a * 3  # Element-wise multiplication
e = np.sqrt(a)  # Element-wise square root
dot_product = np.dot(a, a)  # Dot product

print("Addition:", c)
print("Multiplication:", d)
print("Square root:", e)
print("Dot product:", dot_product)

# 3. Array Indexing and Slicing
print("\n3. Array Indexing and Slicing")
print("First element of a:", a[0])
print("Last two elements of a:", a[-2:])
print("Middle row of b:\n", b[1, :])
print("First column of b:\n", b[:, 0])

# 4. Array Manipulation
print("\n4. Array Manipulation")
reshaped = b.reshape(3, 2)  # Reshape array
flattened = b.flatten()  # Flatten array
transposed = b.T  # Transpose array
concatenated = np.concatenate((a, arange))  # Concatenate arrays

print("Reshaped b:\n", reshaped)
print("Flattened b:", flattened)
print("Transposed b:\n", transposed)
print("Concatenated:", concatenated)

# 5. Mathematical and Statistical Functions
print("\n5. Mathematical and Statistical Functions")
mean = np.mean(a)  # Mean
std = np.std(a)  # Standard deviation
sum_array = np.sum(b)  # Sum of all elements
max_val = np.max(a)  # Maximum value
min_val = np.min(a)  # Minimum value

print("Mean of a:", mean)
print("Standard deviation of a:", std)
print("Sum of b:", sum_array)
print("Max of a:", max_val)
print("Min of a:", min_val)

# 6. Random Number Generation
print("\n6. Random Number Generation")
random_array = np.random.rand(2, 3)  # Random numbers between 0 and 1
random_ints = np.random.randint(1, 10, size=(2, 2))  # Random integers
normal_dist = np.random.normal(loc=0, scale=1, size=5)  # Normal distribution

print("Random array:\n", random_array)
print("Random integers:\n", random_ints)
print("Normal distribution:", normal_dist)

# 7. Linear Algebra
print("\n7. Linear Algebra")
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.matmul(matrix_a, matrix_b)  # Matrix multiplication
determinant = np.linalg.det(matrix_a)  # Determinant
inverse = np.linalg.inv(matrix_a)  # Inverse

print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)
print("Matrix product:\n", matrix_product)
print("Determinant of A:", determinant)
print("Inverse of A:\n", inverse)

# 8. Broadcasting
print("\n8. Broadcasting")
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_1d = np.array([10, 20, 30])
broadcasted_sum = array_2d + array_1d  # Broadcasting

print("2D array:\n", array_2d)
print("1D array:", array_1d)
print("Broadcasted sum:\n", broadcasted_sum)

# 9. Masked Arrays
print("\n9. Masked Arrays")
data = np.array([1, 2, np.nan, 4, 5])
masked_data = np.ma.masked_invalid(data)  # Mask invalid values (NaN)
mean_valid = np.mean(masked_data)  # Mean of valid data

print("Data with NaN:", data)
print("Masked data:", masked_data)
print("Mean of valid data:", mean_valid)

# 10. Polynomial Fitting
print("\n10. Polynomial Fitting")
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])
coefficients = np.polyfit(x, y, 2)  # Fit a 2nd degree polynomial
poly = np.poly1d(coefficients)  # Create polynomial object
evaluated = poly([5, 6])  # Evaluate polynomial at x=5 and x=6

print("x:", x)
print("y:", y)
print("Polynomial coefficients:", coefficients)
print("Evaluated at x=5 and x=6:", evaluated)

# 11. Structured Arrays
print("\n11. Structured Arrays")
dtype = [('name', 'U10'), ('age', 'i4'), ('height', 'f4')]
structured_array = np.array([('Alice', 25, 5.5), ('Bob', 30, 6.0)], dtype=dtype)

print("Structured array:", structured_array)
print("Names:", structured_array['name'])
print("Ages:", structured_array['age'])
print("Heights:", structured_array['height'])

# 12. Saving and Loading Arrays
print("\n12. Saving and Loading Arrays")
array_to_save = np.array([1, 2, 3, 4, 5])
np.save('saved_array.npy', array_to_save)  # Save array to file
loaded_array = np.load('saved_array.npy')  # Load array from file

print("Saved array:", array_to_save)
print("Loaded array:", loaded_array)

# 13. Fast Fourier Transform (FFT)
print("\n13. Fast Fourier Transform (FFT)")
signal = np.array([0, 1, 0, -1])  # Simple signal
fft_result = np.fft.fft(signal)  # Compute FFT
frequencies = np.fft.fftfreq(len(signal))

print("Original signal:", signal)
print("FFT result:", fft_result)
print("Frequencies:", frequencies)

# 14. Histogram Computation
print("\n14. Histogram Computation")
data_for_hist = np.array([1, 2, 2, 3, 3, 3, 4, 4, 5])
hist, bin_edges = np.histogram(data_for_hist, bins=5)

print("Data:", data_for_hist)
print("Histogram:", hist)
print("Bin edges:", bin_edges)

# 15. Conditional Operations with Where
print("\n15. Conditional Operations with Where")
values = np.array([10, -5, 7, -3, 2])
positive_values = np.where(values > 0, values, 0)  # Replace negatives with 0

print("Original values:", values)
print("Positive values only:", positive_values)

# 16. Sorting Arrays
print("\n16. Sorting Arrays")
unsorted_array = np.array([5, 2, 9, 1, 5, 6])
sorted_array = np.sort(unsorted_array)
sorted_indices = np.argsort(unsorted_array)

print("Unsorted array:", unsorted_array)
print("Sorted array:", sorted_array)
print("Indices for sorting:", sorted_indices)

# 17. Unique Value Extraction
print("\n17. Unique Value Extraction")
array_with_duplicates = np.array([1, 2, 2, 3, 3, 3, 4])
unique_values = np.unique(array_with_duplicates)

print("Array with duplicates:", array_with_duplicates)
print("Unique values:", unique_values)