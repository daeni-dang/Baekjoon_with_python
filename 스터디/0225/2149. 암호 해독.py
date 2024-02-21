import sys
input = sys.stdin.readline

def solution(keyStr, encoded):
    answer = [""] * len(encoded)
    n, m = len(encoded) // len(keyStr), len(keyStr)
    board = [[""] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            board[i][j] = encoded[i + j * n]
    keyList = []
    for i in range(m):
        keyList.append([keyStr[i], i])
    keyList.sort()
    for i in range(n):
        for j in range(m):
            answer[i * m + keyList[j][1]] = board[i][j]
    return ''.join(answer)
    
def main():
    keyStr = input().strip()
    encoded = input().strip()
    print(solution(keyStr, encoded))

if __name__ == "__main__":
    main()