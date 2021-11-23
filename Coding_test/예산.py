def solution(d, budget):
    d.sort()
    cnt = 0
    answer = 0
    for i in d:
        if budget >= i:
            budget -= i
            cnt += 1
        else:
            break
    answer = cnt
    return answer


d = [2,2,3,3]
budget = 10
solution(d,budget)