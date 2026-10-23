import torch

# 1. Create a scalar
scalar = torch.tensor(5)

# 2. Create a vector
vector = torch.tensor([1, 2, 3])

# 3. Create a matrix
matrix = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])

# Inspect each tensor
print("Scalar:", scalar)
print("Vector:", vector)
print("Matrix:", matrix)

print("Scalar shape:", scalar.shape)
print("Vector shape:", vector.shape)
print("Matrix shape:", matrix.shape)

print("Matrix dimensions:", matrix.ndim)
print("Matrix data type:", matrix.dtype)