# lists.py
# Link: https://www.hackerrank.com/challenges/python-lists

def carryOp(cmd, A):
    cmd=cmd.strip().split(' ')
    if cmd[0]=="insert":
        A.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0]=="print":
        print(A)
    elif cmd[0]=="remove":
        A.remove(int(cmd[1]))
    elif cmd[0]=="append":
        A.append(int(cmd[1]))
    elif cmd[0]=="sort":
        A.sort()
    elif cmd[0]=="pop":
        A.pop()
    elif cmd[0]=="reverse":
        A.reverse()
    return A

if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        A=carryOp(input(),A)
