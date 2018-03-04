# runner_up.py
# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort()
    highest=max(arr)
    secondHighest = highest
    while secondHighest == highest:
        arr.pop()
        secondHighest = max(arr)
    print(secondHighest)
