import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def findHeights(N, board):
    heights = set()
    for i in range(N):
        for j in range(N):
            heights.add(board[i][j])
    return list(heights)

def dfs(x, y, flooded, N, visited):
    if x < N and x >= 0 and y < N and y >= 0:
        if not visited[x][y] and flooded[x][y] == 0:
            visited[x][y] = True
            dfs(x + 1, y, flooded, N, visited)
            dfs(x - 1, y, flooded, N, visited)
            dfs(x, y + 1, flooded, N, visited)
            dfs(x, y - 1, flooded, N, visited)

def solution(N, board):
    heights = findHeights(N, board)
    if len(heights) == 1:
        return 1
    flooded = [[0] * N for _ in range(N)]
    answer = 0
    for height in heights:
        cnt = 0
        for i in range(N):
            for j in range(N):
                if board[i][j] <= height:
                    flooded[i][j] = 1
                else:
                    flooded[i][j] = 0
            
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and flooded[i][j] == 0:
                    cnt += 1
                    dfs(i, j, flooded, N, visited)
        answer = max(answer, cnt)
    return answer
            

def main():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    print(solution(N, board))

if __name__ == "__main__":
    main()