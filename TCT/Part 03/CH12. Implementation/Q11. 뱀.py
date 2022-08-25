n = int(input()) # n*n 보드의 크기
k = int(input()) # 사과의 개수
board = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(k): # 사과 위치
    tmp = list(map(int, input().split()))
    board[tmp[0]][tmp[1]] = 1

L = int(input()) # 뱀 방향 변환 횟수
snake = {}       # 초, 방향 딕셔너리로 저장
for i in range(L):
    tmp = list(map(str, input().split()))
    snake[int(tmp[0])] = tmp[1]

# 방향 : 1 더하면 왼쪽 회전, 1 빼면 오른쪽 회전
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

curX, curY = 1, 1
board[curX][curY] = 2
q = []
q.append([curX, curY])
cur_dir = 0
sec = 0

while True:
    if sec in snake:
        if snake[sec] == 'L':
            cur_dir = (cur_dir + 1) % 4
        else: cur_dir = (cur_dir - 1) % 4
    nx = curX + dx[cur_dir]
    ny = curY + dy[cur_dir]
    if nx > n or ny > n or nx < 1 or ny < 1:
        break
    curX = nx
    curY = ny
    if board[curX][curY] == 1:
        q.append([curX, curY])
        board[curX][curY] = 2
    elif board[curX][curY] == 2:
        break
    else:
        q.append([curX, curY])
        board[curX][curY] = 2
        tmp = q.pop(0)
        board[tmp[0]][tmp[1]] = 0
    sec += 1
print(sec + 1)