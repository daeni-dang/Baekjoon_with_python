import sys
input = sys.stdin.readline

S = set()
M = int(input())
for _ in range(M):
    tmp = input().strip().split()
    if len(tmp) == 1:
        if tmp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        op, n = tmp[0], tmp[1]
        n = int(n)
        if op == "add":
            S.add(n)
        elif op == "remove":
            S.discard(n)
        elif op == "check":
            print(1 if n in S else 0)
        else:
            if n in S:
                S.remove(n)
            else:
                S.add(n)