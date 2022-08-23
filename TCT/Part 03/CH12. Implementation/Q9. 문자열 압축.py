'''
    1부터 문자열/2 크기까지 압축하는 크기를 늘려가면서 압축
    가장 길이가 짧은 것 선택
    
    1. 압축 길이 1부터 (문자열 길이) / 2까지 반복
    2. 압축 길이로 문자열 압축하여 배열에 저장
        2-1. 압축된 문자열과 다음 문자열(압축된 문자열 길이만큼)과 비교하여 같으면 압축 개수 증가
        2-2. 다르다면 압축 개수 초기화
'''

s = input()
answer = []

for press in range(1, len(s) // 2 + 1):
    tmp = ""
    num = 1
    prev = s[:press]
    for i in range(press, len(s), press):
        if s[i:i+press] == prev:
            num += 1
        else:
            if num > 1:
                tmp += str(num) + prev
            else: 
                tmp += prev
                prev = s[i:i+press]
            num = 1
    if num > 1:
        tmp += str(num) + prev
    else: 
        tmp += prev
        prev = s[i:i+press]
    answer.append(tmp)

answer.sort(key=lambda x : len(x))
print(len(answer[0]))