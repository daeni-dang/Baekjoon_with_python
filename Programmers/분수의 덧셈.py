def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = lcm(denom1, denom2)
    numer1 *= denom // denom1
    numer2 *= denom // denom2
    numer = numer1 + numer2
    
    for i in range(max(numer, denom), 0, -1):
        if numer % i == 0 and denom % i == 0:
            answer.append(numer//i)
            answer.append(denom//i)
            break
    
    return answer