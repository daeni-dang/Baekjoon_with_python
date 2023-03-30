# 92.6점

def bingo(board, check):
    for i in range(3):
        col_cnt, row_cnt = 0, 0
        for j in range(3):
            if board[i][j] == check:
                col_cnt += 1
        if col_cnt == 3:
            return True
        for j in range(3):
            if board[j][i] == check:
                row_cnt += 1
        if row_cnt == 3:
            return True
    right_cnt, left_cnt = 0, 0
    for i in range(3):
        if board[i][i] == check:
            right_cnt += 1
        if board[2 - i][2 - i] == check:
            left_cnt += 1
    if right_cnt == 3 or left_cnt == 3:
        return True
    return False

def solution(board):
    check = {"O":[], "X":[]}
    for row, b in enumerate(board):
        for col, i in enumerate(b):
            try: check[i].append([row, col])
            except: pass
    if len(check["O"]) < len(check["X"]):
        return 0
    elif len(check["O"]) == len(check["X"]):
        if bingo(board, "O"):
            return 0
    elif len(check["O"]) == len(check["X"]) + 1:
        if bingo(board, "X"):
            return 0
    elif len(check["O"]) > len(check["X"]) + 1:
        return 0
    return 1