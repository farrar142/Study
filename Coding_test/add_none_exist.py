numbers = [1,2,3,4,6,7,8,0]

def solution(numbers):
    compare = [x for x in range(0,10)]
    return sum(list(set(compare).difference(set(numbers))))

solution(numbers)