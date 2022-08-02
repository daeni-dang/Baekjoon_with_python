n, m = map(int, input().split())
x, y, d = map(int, input().split())
game_map = []
d_list = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}
for _ in range(n):
    tmp = list(map(int, input().split()))
    game_map.append(tmp)
answer = 1
visit = 0
while True:
    # 현재 방향을 기준으로 왼쪽 방향부터 갈 곳 결정하므로 
    # 반시계 방향으로 한 번 회전
    if d == 0: d = 3
    else: d -= 1
    # 반시계 방향으로 회전하면서 육지(0)가 있다면 이
    # 이전 위치는 가본 위치(2)로 변경
    game_map[x][y] = 2
    if game_map[x + d_list[d][0]][y + d_list[d][1]] == 0:
        x += d_list[d][0]
        y += d_list[d][1]
        answer += 1
        visit = 0
    else:
        visit += 1
    # 네 방향 모두 이미 가본 칸이거나 바다인 경우
    # 바라보는 방향 유지한 채로 한칸 뒤로 이동
    if visit == 4:
        x += d_list[(d + 2) % 4][0]
        y += d_list[(d + 2) % 4][1]
        visit = 0
        # 뒤쪽 방향이 바다라면 종료
        if game_map[x][y] == 1:
            break
print(answer)