import sys
input = sys.stdin.readline

def backTracking(depth, j, v, c, L, C, chars):
    global arr
    if depth == L:
        if v >= 1 and c >= 2:
            print(''.join(arr))
        return
    for i in range(j, C):
        arr.append(chars[i])
        if chars[i] == 'a' or chars[i] == 'e' or chars[i] == 'i' or chars[i] == 'o' or chars[i] == 'u':
            backTracking(depth + 1, i + 1, v + 1, c, L, C, chars)
        else:
            backTracking(depth + 1, i + 1, v, c + 1, L, C, chars)
        arr.pop()

def solution(L, C, chars):
    backTracking(0, 0, 0, 0, L, C, chars)

def main():
    L, C = map(int, input().split())
    chars = list(input().strip().split())
    chars.sort()
    solution(L, C, chars)

if __name__ == "__main__":
    arr = []
    main()