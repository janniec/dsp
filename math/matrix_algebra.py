# Matrix Algebra

import numpy as np
import pandas as pd
from scipy import linalg

A = np.matrix([[1, 2, 3], [2, 7, 4]])
B = np.matrix([[1, -1], [0, 1]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])
u = np.array([[6, 2, -3, 5]])
v = np.array([[3, 5, -1, 4]])
w = np.matrix([[1], [8], [0], [5]])

# 1. Matrix Dimensions

# 1.1
A.shape
# (2, 3)

# 1.2
B.shape
# (2, 2)

# 1.3
C.shape
# (3, 2)

# 1.4
D.shape
# (2, 3)

# 1.5
u.shape
# (1, 4)

# 1.6
w.shape
# (4, 1)

# 2. Vector Operations

# 2.1
u + v
# array([[ 9,  7, -4,  9]])

# 2.2
u - v
# array([[ 3, -3, -2,  1]])

# 2.3
alpha = 6
alpha * u
# array([[ 36,  12, -18,  30]])

# 2.4
u.dot(v)
# not defined.

# 2.5
linalg.norm(u)
# 8.6023252670426267

# 3. Matrix Operations

# 3.1
A + C
# not defined

# 3.2
A - C.T
# matrix([[-4, -7, -3],
#        [ 3,  6,  4]])

# 3.3
C.T + (3 * D)
# matrix([[14,  3,  3],
#        [ 2,  7,  9]])

# 3.4
B * A
# matrix([[-1, -5, -1],
#        [ 2,  7,  4]])

# 3.5
B * A.T
# not defined

# 3.6
B * C
# not defined

# 3.7
C * B
# matrix([[ 5, -6],
#        [ 9, -8],
#        [ 6, -6]])

# 3.8
B ** 4
# matrix([[ 1, -4],
#        [ 0,  1]])

# 3.9
A * A.T
# matrix([[14, 28],
#        [28, 69]])

#3.10
D.T * D
# matrix([[10, -4,  0],
#        [-4,  8,  8],
#        [ 0,  8, 10]])
