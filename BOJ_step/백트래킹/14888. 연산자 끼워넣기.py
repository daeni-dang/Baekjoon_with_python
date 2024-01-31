minimum = 1000000000
maximum = -1000000000

def back(num, i, plus, minus, mul, div):
    global minimum, maximum
    if i == N:
        maximum = max(maximum, num)
        minimum = min(minimum, num)
        return
    if plus:  # +
        back(num + nums[i], i + 1, plus - 1, minus, mul, div)
    if minus:  # -
        back(num - nums[i], i + 1, plus, minus - 1, mul, div)
    if mul:  # *
        back(num * nums[i], i + 1, plus, minus, mul - 1, div)
    if div:  # /
        back(int(num / nums[i]), i + 1, plus, minus, mul, div - 1)

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    op = list(map(int, input().split()))
    back(nums[0], 1, op[0], op[1], op[2], op[3])
    print(maximum)
    print(minimum)