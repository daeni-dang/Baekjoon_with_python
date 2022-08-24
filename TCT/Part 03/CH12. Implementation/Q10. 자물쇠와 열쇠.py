def rotate(arr):
    n = len(arr)
    rot_arr = [([0] * n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rot_arr[j][n - i - 1] = arr[i][j]
    return rot_arr

def insert_key(arr, key, x, y):
    n = len(arr)
    insert_arr = [([0] * n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            insert_arr[i][j] = arr[i][j]
    for i in range(x, x + len(key)):
        for j in range(y, y + len(key)):
            insert_arr[i][j] += key[i - x][j - y]
    return insert_arr

def check(arr):
    n = len(arr) // 3
    for i in range(n):
        for j in range(n):
            if arr[i + n][j + n] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    result = [([0] * (n * 3)) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            result[i + n][j + n] = lock[i][j]
    for _ in range(4):
        key = rotate(key)
        for i in range(n * 2 + 1):
            for j in range(n * 2 + 1):
                insert_arr = insert_key(result, key, i, j)
                if check(insert_arr):
                    return True
    return False