'''
zip : 여러 개의 iterable을 동시에 순환
zip 함수는 서로 길이가 다른 리스트에서 짧은 길이만큼만 반복한다.
'''

def solution(mylist):
    return list(zip(*mylist))

def solution(mylist):
    answer = []
    for first, second in zip(mylist, mylist[1:]):
        answer.append(abs(first - second))
    return answer