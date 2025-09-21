import sys

S = []
N = int(input())

for i in range(N):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        str = command[0]
        num = int(command[1])
    else:
        str = command[0]
    if str == "add":
        if num not in S:
            S.append(num)
        else:
            continue
    elif str == "remove":
        if num in S:
            S.remove(num)
        else:
            continue
    elif str == "check":
        if num in S:
            print(1)
        else:
            print(0)
    elif str == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.append(num)    
    elif str == "all":
        S = list(range(1, 21))
    elif str == "empty":
        S = []
