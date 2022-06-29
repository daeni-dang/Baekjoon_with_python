n, m = map(int, input().split())
board = [input() for i in range(n)]

def check(i, j):
    color = ['B', 'W']
    answer = []
    for s in range(2):
        tmp_ans = 0
        for r in range(i, i + 8):
            color_idx = s
            if r % 2 == 0:
                for c in range(j, j + 8):
                    if board[r][c] != color[color_idx % 2]:
                        tmp_ans += 1
                    color_idx += 1
            elif r % 2 == 1:
                color_idx += 1
                for c in range(j, j + 8):
                    if board[r][c] != color[color_idx % 2]:
                        tmp_ans += 1
                    color_idx += 1
        answer.append(tmp_ans)
    return answer

arr_answer = []
answer = []

for i in range(n - 7):
    for j in range(m - 7):
        arr_answer.append(check(i, j))
for i in arr_answer:
    for j in i:
        answer.append(j)
print(min(answer))