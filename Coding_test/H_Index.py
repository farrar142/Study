def solution(citations):
    _citations = {}
    answer = 0
    for i in citations:
        for j in range(0,i+1):
            if j in _citations:
                _citations[j] += 1
            else:
                _citations[j] = 1
    for i in range(0,max(citations)+1):
        if i <= _citations[i]:
            if i >= answer:
                answer = i
    return answer


citations = [0,1,1]
solution(citations)