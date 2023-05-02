def mul(A, B, N):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000
    return result

def solution(A, B, N):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    tmp = solution(A, B // 2, N)
    if B % 2 == 1:
        return mul(mul(tmp, tmp, N), A, N)
    else:
        return mul(tmp, tmp, N)

if __name__ == "__main__":
    N, B = map(int, input().split())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))

    result = solution(matrix, B, N)
    for i in range(N):
        for j in range(N):
            print(result[i][j], end=' ')
        print()