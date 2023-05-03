if __name__ == "__main__":
    n = int(input())
    m = 1000000
    p = 15 * (m // 10)
    fibo = [0, 1] + [0] * p
    for i in range(2, p):
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) % m
    print(fibo[n % p])