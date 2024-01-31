import sys
input = sys.stdin.readline

N, M = map(int, input().split())
stored = {}
for _ in range(N):
    site, pwd = map(str, input().split())
    stored[site] = pwd
for _ in range(M):
    site = input().strip()
    print(stored[site])