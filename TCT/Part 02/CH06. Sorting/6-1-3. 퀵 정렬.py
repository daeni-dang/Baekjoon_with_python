array = list(map(int, input().split()))

def quick_sort(array, start, end):
    if start >= end:
        return
    left = start + 1
    right = end
    while left <= right:
        pivot = start
        while left <= right and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    
quick_sort(array, 0, len(array) - 1)
print(array)