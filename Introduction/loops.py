# loops.py
# Link: https://www.hackerrank.com/challenges/python-loops/problem

if __name__ == '__main__':
    n = int(input())
    print('\n'.join([str(i**2) for i in range(n)]))
