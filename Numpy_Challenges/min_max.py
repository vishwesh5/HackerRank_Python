# min_max.py
# Link: https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy as np
N,M = [int(i) for i in (input()).split(' ')]
A = []
for i in range(N):
    A.append([int(i) for i in (input()).split(' ')])
A = np.array(A)
print(np.max(np.min(A,axis=1),axis=None))
