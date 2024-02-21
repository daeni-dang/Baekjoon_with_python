import sys
input = sys.stdin.readline

def solution(s, t):
    sidx = 0
    check = 0
    for i in range(len(t)):
        if sidx >= len(s):
            break
        if s[sidx] == t[i]:
            sidx += 1
            check += 1
    if check >= len(s):
        return "Yes"
    return "No"

def main():
    while True:
        try:
            s, t = input().strip().split()
            print(solution(s, t))
        except:
            break

if __name__ == "__main__":
    main()