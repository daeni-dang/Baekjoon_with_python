import sys
input = sys.stdin.readline

def main():
    answer = 0
    N, L = map(int, input().split())
    loc = list(map(int, input().split()))
    loc.sort()
    pipe = [0] * 1001
    for i in loc:
        pipe[i] = 1
    for l in loc:
        if pipe[l] == 1:
            answer += 1
            tmpL = L - 0.5
            i = l
            while tmpL >= 0.5 and i < 1001:
                pipe[i] = 0
                tmpL -= 1
                i += 1
    print(answer)
        

if __name__ == "__main__":
    main()