# array_math.py
# Link: https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy as np
n,m=(input()).split(' ')
n,m=int(n),int(m)
A,B=[],[]
for i in range(n):
    A.append([int(t) for t in (input()).split(' ')])
for i in range(n):
    B.append([int(t) for t in (input()).split(' ')])
A,B=np.array(A),np.array(B)
print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B))
print(A//B)
print(np.mod(A,B))
print(np.power(A,B))
