import sys
input = sys.stdin.readline

def main():
    numbers = [(i * (i + 1)) // 2 for i in range(1, 45)]
    isEureka = [0] * 1001
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k <= 1000:
                    isEureka[i + j + k] = 1
    T = int(input())
    for _ in range(T):
        sys.stdout.write(str(isEureka[int(input())]) + "\n")

if __name__ == "__main__":
    main()


# def dupliPermutation(k, arr, depth, numbers, answer, ai):
#     if depth == 3:
#         sums = 0
#         for i in range(3):
#             sums += numbers[arr[i]]
#         if sums == k:
#             answer[ai] = 1
#         return
#     for i in range(1, 46):
#         arr[depth] = i
#         dupliPermutation(k, arr, depth + 1, numbers, answer, ai)

# def main():
#     T = int(input())
#     numbers = [(i * (i + 1)) // 2 for i in range(46)]
#     ks = []
#     for _ in range(T):
#         ks.append(int(input()))
#     answer = [0] * T
#     for i in range(T):
#         arr = [0, 0, 0]
#         dupliPermutation(ks[i], arr, 0, numbers, answer, i)
#     for i in answer:
#         print(i)