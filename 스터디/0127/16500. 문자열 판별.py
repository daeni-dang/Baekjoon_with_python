import sys
input = sys.stdin.readline

def solution(S, A, n):
    sn = len(S)
    canmake = [0] * sn
    i = 0
    while i < sn:
        for j in range(n):
            if i < sn and S[i] == A[j][0]:
                if i + len(A[j]) > sn:
                    i += len(A[j])
                    break
                for k in range(len(A[j])):
                    if S[i + k] == A[j][k]:
                        canmake[i + k] = 1
                i += len(A[j])
    for i in range(sn):
        if canmake[i] == 0:
            return 0
    return 1


def main():
    S = input().strip()
    n = int(input())
    A = []
    for _ in range(n):
        A.append(input().strip())
    print(solution(S, A, n))

if __name__ == "__main__":
    main()