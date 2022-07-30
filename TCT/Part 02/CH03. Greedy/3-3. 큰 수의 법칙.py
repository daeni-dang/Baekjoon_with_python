'''
    n : 입력되는 숫자의 개수
    m : 숫자를 더하는 횟수
    k : 연속하여 더해질 수 있는 횟수
    
    1. 가장 큰 수, 두번째로 큰 수 찾기(정렬)
    2. 덧셈
        2-1. k번만큼 첫 번째 원소(가장 큰 수) 덧셈
        2-2. 두 번째 원소 1번 덧셈
'''

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
arr.sort()

# 가장 큰 수가 나오는 횟수
big = (m // (k + 1)) * k
# 나누어떨어지지 않는 경우
big += m % (k + 1)

answer += big * arr[n - 1]
answer += (m - big) * arr[n - 2]

print(answer)