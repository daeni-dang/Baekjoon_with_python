from itertools import permutations

def find_prime(numbers):
    max_number = int("9"*len(numbers))
    prime = [True] * (max_number + 1)
    prime[0] = False
    prime[1] = False
    
    for i in range(2, max_number+1):
        if prime[i]:
            for j in range(i*2, max_number+1, i):
                prime[j] = False
    return prime

def solution(numbers):
    answer = 0
    prime = find_prime(numbers)
    each = []
    for i in numbers:
        each.append(i)
    perm = []
    for i in range(len(each)):
        perm.append(list(permutations(each, i + 1)))
    perm = sum(perm, [])
    result = []
    for i in perm:
        result.append(''.join(list(i)))
    result = map(int, result)
    result = list(set(result))
    for i in result:
        if prime[int(i)] == True:
            answer += 1
    return answer