import sys
input = sys.stdin.readline

def compare(answer, guess):
    strike, ball = 0, 0
    for i in range(3):
        for j in range(3):
            if answer[i] == guess[j]:
                if i != j:
                    ball += 1
                if i == j:
                    strike += 1
    return strike, ball

def main():
    n = int(input())
    guesses = []
    answer = set()
    for _ in range(n):
        guesses.append(list(map(int, input().split())))
    candidates = [[] for _ in range(n)]
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i != j and j != k and i != k:
                    num = int(str(i) + str(j) + str(k))
                    for l, (guess, strike, ball) in enumerate(guesses):
                        s, b = compare(str(num), str(guess))
                        if strike == s and ball == b:
                            candidates[l].append(num)

    answer = set(candidates[0])
    for i in range(1, n):
        answer = answer & set(candidates[i])
    print(len(answer))

if __name__ == "__main__":
    main()