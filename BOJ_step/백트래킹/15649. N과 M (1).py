N, M = map(int, input().split())

s = []

def solution():
    if len(s) == M:
        print(' '.join(s))
        return
    for i in range(1, N + 1):
        if str(i) not in s:
            s.append(str(i))
            solution()
            s.pop()
    
solution()