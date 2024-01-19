'''
    참고 : https://velog.io/@dlgosla/%EB%B0%B1%EC%A4%80-BOJ-13904-%EA%B3%BC%EC%A0%9C-python
'''

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    assigns = []
    maxDay = 0
    for _ in range(N):
        assigns.append(list(map(int, input().split())))
        maxDay = max(maxDay, assigns[-1][0])
    assigns.sort(key=lambda x: -x[1])
    days = [0] * (maxDay + 1)
    for assign in assigns:
        day = assign[0]
        while day > 0:
            if days[day] == 0:
                days[day] = assign[1]
                break
            day -= 1
    print(sum(days))

if __name__ == "__main__":
    main()