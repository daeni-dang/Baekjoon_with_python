'''
map
'''

def solution(mylist):
    answer = []
    # 단순 방법
    for i in mylist:
        answer.append(int(i))
    # map을 이용한 풀이
    answer = list(map(int, mylist))
    return answer


def solution(mylist):
    answer = list(map(len, mylist))
    return answer