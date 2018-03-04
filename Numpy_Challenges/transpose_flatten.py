# transpose_flatten.py
# Link: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy as np
N,M = [int(i) for i in input().strip().split(' ')]
A = []
for i in range(N):
    A.append([int(i) for i in input().strip().split(' ')])
A = np.array(A)
print(np.transpose(A))
print(A.flatten())
