def yak(x):
    yak = []
    for i in range(1,x+1):
        if x%i == 0:
            yak.append(i)
    return len(yak)
def solution(left,right):
    answer = 0
    for i in range(left,right+1):
        if yak(i)%2 == 0:
            answer += i
        else:
            answer -= i
    return answer
solution(13,17)