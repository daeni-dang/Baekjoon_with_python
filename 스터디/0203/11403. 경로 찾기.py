import sys
input = sys.stdin.readline

def dfs(x, y, matrix, visited, N, answer):
    for i in range(N):
        if matrix[x][i] == 1:
            if i == y:
                answer[x][y] = 1
            dfs(i, y, matrix, visited, N, answer)

def solution(N, matrix):
    answer = [[0] * N for _ in range(N)]
    visited = [False] * N
    for i in range(N):
        for j in range(N):
            dfs(i, j, matrix, visited, N, answer)
    return answer
            

def main():
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    print(solution(N, matrix))

if __name__ == "__main__":
    main()