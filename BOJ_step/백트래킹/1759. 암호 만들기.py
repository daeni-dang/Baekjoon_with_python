L, C = map(int, input().split())
alp = list(input().split())
alp.sort()

password = []
def solution(depth):
    if depth == L:
        vowel, consonant = 0, 0
        for i in password:
            if i in "aeiou":
                vowel += 1
            else:
                consonant += 1
        if vowel >= 1 and consonant >= 2:
            print("".join(password))
                
        return
    for i in range(C):
        if len(password) == 0 or alp[i] > password[-1]:
            password.append(alp[i])
            solution(depth + 1)
            password.pop()

solution(0)