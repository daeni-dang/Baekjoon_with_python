def virus(lab):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = [[0] * len(lab[0]) for _ in range(len(lab))]
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            result[i][j] = lab[i][j]
    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j] == 2:
                def dfs(x, y):
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < n and ny < m and nx >= 0 and ny >= 0:
                            if result[nx][ny] == 0:
                                result[nx][ny] = 2
                                dfs(nx, ny)
                dfs(i, j)
    # for i in result:
    #     print(i)
    # print()
    cnt = 0
    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j] == 0:
                cnt += 1
    return cnt

answer = 0
def solution(lab, wall):
    # 임의로 세 개 벽을 세우고
    # 바이러스가 있는 모든 지점에서 bfs (visited 체크)
    # 바이러스가 퍼질 수 있는 공간에 2로 표시
    # 최종 map에서 2의 개수 세기
    global answer
    if wall == 3:
        cnt = virus(lab)
        if cnt > answer:
            answer = cnt
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall += 1
                solution(lab, wall)
                wall -= 1
                lab[i][j] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    lab = []
    for i in range(n):
        lab.append(list(map(int, input().split())))
    solution(lab, 0)
    print(answer)