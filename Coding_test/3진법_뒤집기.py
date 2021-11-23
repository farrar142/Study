def solution(n):
    third = []
    while n>=1:
        third.append(n%3)
        n = n//3
    answer = 0
    counter = 1
    for i in third[::-1]:
        answer = answer + i*counter
        counter *= 3       
    return answer

n = 45
solution(n)