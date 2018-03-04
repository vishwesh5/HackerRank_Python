# eye_identity.py
# Link: https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy as np
N,M=[int(i) for i in input().strip().split(' ')]
print(np.eye(N,M,k=0))
