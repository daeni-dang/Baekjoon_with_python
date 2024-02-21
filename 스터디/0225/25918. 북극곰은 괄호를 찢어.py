import sys
input = sys.stdin.readline

def solution(N, S):
    answer = 0
    cnt = 0
    stack = []
    for s in S:
        if answer < cnt:
            answer = cnt
        if stack and ((s == '(' and stack[-1] == ')') or (s == ')' and stack[-1] == '(')):
            stack.pop()
            cnt -= 1
        else:
            stack.append(s)
            cnt += 1
    return answer if cnt == 0 else -1

def main():
    N = int(input())
    S = input().strip()
    print(solution(N, S))

if __name__ == "__main__":
    main()