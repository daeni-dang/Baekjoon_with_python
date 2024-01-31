from copy import deepcopy

type = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
    ]

# 위, 오, 아, 왼
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def watch(temp, c, x, y):
    for i in c:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                break
            if temp[nx][ny] == 6:
                break
            else:
                temp[nx][ny] = 7
            

def solution(depth, arr):
    global answer
    if depth == num:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    cnt += 1
        answer = min(answer, cnt)
        return
    temp = deepcopy(arr)
    c, x, y = cctv[depth]
    for i in type[c]:
        watch(temp, i, x, y)
        solution(depth + 1, temp)
        temp = deepcopy(arr)

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

num = 0 # cctv 개수
cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            num += 1
            cctv.append([board[i][j], i, j])
answer = 1e9
solution(0, board)
print(answer)