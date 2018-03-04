# mean_var_std.py
# Link: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy as np
A=[]
for i in range([int(i) for i in (input()).split(' ')][0]):
    A.append([int(i) for i in (input()).split(' ')])
A = np.array(A)
print(np.mean(A,axis=1))
print(np.var(A,axis=0))
print(np.std(A))
