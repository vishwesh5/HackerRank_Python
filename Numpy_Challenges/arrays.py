# arrays.py
# Link: https://www.hackerrank.com/challenges/np-arrays/problem

def arrays(arr):
    # complete this function
    # use numpy.array 
    arr = numpy.array([float(i) for i in arr][::-1],float)
    return arr
