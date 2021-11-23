
def solution(n):
    result = []
    while n:
        t = n % 3
        if not t:
            print(t)
            t = 3
            n -= 1
            print(n)
        result.append(str(t))
        n //= 3  
    for i in range(len(result)):
        if result[i] == '3':
            result[i] = '4'
    return ''.join(result[::-1])


print(solution(10))