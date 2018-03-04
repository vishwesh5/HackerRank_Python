# concatenate.py
# Link: https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy as np
N,M,P=[int(i) for i in input().strip().split(' ')]
A=[]
B=[]
for i in range(N):
    A.append([int(j) for j in input().strip().split(' ')])
for i in range(M):
    B.append([int(j) for j in input().strip().split(' ')])
A,B=np.array(A),np.array(B)
print(np.concatenate((A,B),axis=0))
