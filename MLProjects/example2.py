import numpy as np
from scipy import sparse


# Create a 2D Numpy array with diagonal of ones, and zeros everywhere else

eye = np.eye(4)
print("NumPy array:\n{}".format(eye))

# Convert the Numpy array to a SciPy sparse matrix in CSR format
# Only the nonzero entries are stored

sparse_matrix = sparse.csr_matrix(eye)
print("\nScipy sparse CSR matrix:\n{}".format(sparse_matrix))