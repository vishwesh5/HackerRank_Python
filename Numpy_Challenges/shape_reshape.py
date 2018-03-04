# shape_reshape.py
# Link: https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy as np
print(np.reshape(np.array([int(i) for i in input().strip().split(' ')]),(3,3)))
