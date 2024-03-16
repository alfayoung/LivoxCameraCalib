import numpy as np

yaw = np.deg2rad(10)

R1 = np.array([
    [np.cos(-yaw), -np.sin(-yaw), 0],
    [np.sin(-yaw), np.cos(-yaw), 0],
    [0, 0, 1]
])

R2 = np.array([
    [np.cos(yaw), 0, np.sin(yaw)],
    [0, 1, 0],
    [-np.sin(yaw), 0, np.cos(yaw)]
])

# Given matrix
M1 = np.array([
    [0, -1, 0],
    [0, 0, -1],
    [1, 0, 0]
])

M2 = np.array([
    [0, 0, 1],
    [-1, 0, 0],
    [0, -1, 0]
])

# Multiply rotation matrix with given matrix
result1 = np.dot(M1, R1)

result2 = np.dot(M2, R2)

print(f"result1 = {result1}")

print(f"result2 = {result2}")

print(np.dot(result1, result2))

for x, y, z in result1:
    print(f"{x}, {y}, {z}, 0,")
print("0, 0, 0, 1")