# floor_ceil_rint.py
# Link: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy as np
A = np.array([float(t) for t in (input()).split(' ')],float)
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))
