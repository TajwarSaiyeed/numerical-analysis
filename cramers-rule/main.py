import numpy as np

A = np.array([
    [1, 1, 1],
    [2, 3, 5],
    [4, 0, 5]
])

c = [5, 8, 2]

dA = np.linalg.det(A)

A_X, A_Y, A_Z = [A.copy() for _ in range(3)] 
A_X[:, 0], A_Y[:, 1], A_Z[:, 2] = [c for _ in range(3)]

dx = np.linalg.det(A_X)
dy = np.linalg.det(A_Y)
dz = np.linalg.det(A_Z)

x = dx / dA
y = dy / dA
z = dz / dA

print(f"X : {x}")
print(f"Y : {y}")
print(f"Z : {z}")


# A_X = A.copy()
# A_X[:, 0] = c

# dX = np.linalg.det(A_X)


# A_Y = A.copy()
# A_Y[:, 1] = c

# dY = np.linalg.det(A_Y)

# x = dX / dA
# y = dY / dA

# print(x)
# print(y)



