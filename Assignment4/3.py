#Write a program to perform matrix multiplication using NumPy.(Hint: Use np.dot() or @ operator).
import numpy as np
# Define two matrices
matrix_a = np.array([[1, 2, 3],
                        [4, 5, 6]])
matrix_b = np.array([[7, 8],                   
                        [9, 10],
                        [11, 12]])
# Perform matrix multiplication
result = np.dot(matrix_a, matrix_b)
# Alternatively, you can use the @ operator
# result = matrix_a @ matrix_b
# Display the result
print(result)

