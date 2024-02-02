import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, students, arr, visited, n):  # n은 arr의 길이
    global answer
    visited[x] = True
    arr.append(x)
    idx = -1
    if visited[students[x]]:
        for i in range(n):
            if arr[i] == students[x]:
                idx = i
        if idx != -1:
            answer -= (n - idx)
        return
    else:
        dfs(students[x], students, arr, visited, n + 1)
    
def solution(n, students):
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            arr = []
            dfs(i, students, arr, visited, 1)
    return answer

def main():
    global answer
    T = int(input())
    for _ in range(T):
        n = int(input())
        answer = n
        students = [0] + list(map(int, input().split()))
        print(solution(n, students))

if __name__ == "__main__":
    answer = 0
    main()