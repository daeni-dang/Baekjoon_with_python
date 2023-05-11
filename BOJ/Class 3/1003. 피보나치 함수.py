import sys
input = sys.stdin.readline
print = sys.stdout.write

def fibonacci(n):
    cnt = [[1, 0], [0, 1]]
    for i in range(2, n + 1):
        cnt.append([cnt[i - 2][0] + cnt[i - 1][0], cnt[i - 2][1] + cnt[i - 1][1]])
    return cnt

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        zero, one = 0, 0
        n = int(input())
        cnt = fibonacci(n)
        print(str(cnt[n][0]) + " " + str(cnt[n][1]) + "\n")