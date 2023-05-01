if __name__ == "__main__":
    a, b, C = map(int, input().split())
    def solution(A, B):
        if B == 1:
            return A % C
        if B % 2 == 1:
            return ((solution(A, B // 2) ** 2) * A) % C
        else:
            return (solution(A, B // 2) ** 2) % C
    print(solution(a, b))