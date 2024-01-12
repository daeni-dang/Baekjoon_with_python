import sys
input = sys.stdin.readline

def combination(answer, dwarfs, arr, depth, j):
    if depth == 7:
        sums = 0
        for i in range(7):
            sums += dwarfs[arr[i]]
        if sums == 100:
            for i in range(7):
                answer[i] = dwarfs[arr[i]]
        return
    for i in range(j, 9):
        arr[depth] = i
        combination(answer, dwarfs, arr, depth + 1, i + 1);

def main():
    answer = [0] * 7
    dwarfs = []
    for _ in range(9):
        dwarfs.append(int(input()))
    arr = [0] * 7
    combination(answer, dwarfs, arr, 0, 0)
    for i in sorted(answer):
        print(i)

if __name__ == "__main__":
    main()