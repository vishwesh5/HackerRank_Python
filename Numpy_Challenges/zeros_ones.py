# zeros_ones.py
# Link: https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
import numpy as np
A = [int(i) for i in input().strip().split(' ')]
print(np.zeros((A),dtype=np.int))
print(np.ones((A),dtype=np.int))
