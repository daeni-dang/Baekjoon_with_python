from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    answer = 1
    n = int(input())
    clothes = defaultdict(int)
    for i in range(n):
        name, type = input().split()
        clothes[type] += 1
    
    arr = []
    for i in clothes.values():
        arr.append(i)
    for i in range(len(arr)):
        answer *= (arr[i] + 1)
    print(answer - 1)