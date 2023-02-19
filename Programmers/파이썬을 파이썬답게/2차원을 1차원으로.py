'''
1. sum 함수
2. itertools.chain
3. itertools와 unpacking
4. list comprehension
5. reduce 함수
'''


def solution(mylist):
    # 방법 1
    answer = sum(mylist, [])
    
    # 방법 2
    import itertools
    answer = list(itertools.chain.from_iterable(mylist))
    
    # 방법 3
    answer = list(itertools.chain(*mylist))
    
    # 방법 4
    answer = [element for array in mylist for element in array]
    
    # 방법 5
    from functools import reduce
    answer = list(reduce(lambda x, y: x + y, mylist))
    import operator
    answer = list(reduce(operator.add, mylist))
    
    return answer