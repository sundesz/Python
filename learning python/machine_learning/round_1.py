import numpy as np
from sklearn import datasets

X = np.arange(1, 101).reshape(20, 5)
a = X[:,0]
b = X[9]
c = X[2:4].reshape(5,2)

# print(X)
# print(a)
# print(b)
# print(c)

# print(f"Shape of X: {X.shape}")
# print(f"Shape of a: {a.shape}")
# print(f"Shape of b: {b.shape}")
# print(f"Shape of c: {c.shape}")

print(datasets.load_linnerud(20,1))

# Store a vector containing the values of the first feature of the feature matrix in the variable a.

# Store the feature vector of the 10th data point in the variable b

# Store a matrix containing the 2nd and 3rd features of data points  10,11,…,14  in the variable c.
# assert a.shape == (20,), "The shape of a is incorrect!"
# assert b.shape == (5,), "The shape of b is incorrect!"
# assert c.shape == (5, 2), "The shape of c is incorrect!"

"""
# Create a matrix A and column vector b
A = np.array([[1,2,3], [4,5,6]])
B = np.array([[9,8,7]]).T

# Print matrices
print(f"A =\n{A}")
print(f"B =\n{B}")

# Use the .shape attribute to get the shapes of A and b
print(f"Shape of A: {A.shape}")
print(f"Shape of B: {B.shape}")

# Get the element in the second row and first column of A
print(f"A_2_1: {A[1,0]}")

# Get second column of A
print(f"A_2: {A[:,1]}")

# Get first row of A
print(f"A_1:  {A[0]}")

# Get columns 2 and 3 of A
print(f"A_C_2_3: {A[:,1:3]}")
"""