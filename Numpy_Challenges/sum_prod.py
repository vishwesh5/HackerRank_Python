# sum_prod.py
# Link: https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy as np
N,M = (input()).split(' ')
N,M = int(N), int(M)
A=[]
for i in range(N):
    A.append([int(t) for t in (input()).split(' ')])
A = np.array(A)
print(np.prod(np.sum(A,axis=0),axis=None))
