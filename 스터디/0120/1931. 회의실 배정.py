import sys
input = sys.stdin.readline

def main():
    answer = 1
    N = int(input())
    meets = []
    maxs = 0
    for _ in range(N):
        meets.append(list(map(int, input().split())))
        maxs = max(maxs, meets[-1][1])
    meets.sort(key=lambda x: (x[1], x[0]))
    bef = meets[0]
    for meet in meets[1:]:
        if meet[0] >= bef[1]:
            answer += 1
            bef = meet
    print(answer)

if __name__ == "__main__":
    main()