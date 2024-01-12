import sys
input = sys.stdin.readline

def combination(n, s, depth, arr, j, number, answer, size):
    if depth == size:
        sums = 0
        for i in range(size):
            sums += number[arr[i]]
        if sums == s:
            answer.append(1)
        return
    for i in range(j, n):
        arr[depth] = i
        combination(n, s, depth + 1, arr, i + 1, number, answer, size)

def main():
    n, s = map(int, input().split())
    number = list(map(int, input().split()))
    arr = [0] * n
    answer = []
    for i in range(0, n):
        combination(n, s, 0, arr, 0, number, answer, i + 1)
    print(len(answer))

if __name__ == "__main__":
    main()