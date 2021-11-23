def solution(answers):
    n = 1
    p1 = []
    p2 = []
    p3 = []
    count = []
    tmp = 0
    winner = 0
    for i in answers:
        if n>=6:
            n = 1
        p1.append(n)
        n += 1
    n = 1
    m = 1
    for i in answers:
        if m>=6:
            m=1
        if n %2 == 1:
            p2.append(2)
        else:
            if m != 2:
                p2.append(m)
                m+=1
            else:
                m+=1
                p2.append(m)
                m+=1
        n+=1
    n = 6
    m = 1
    for i in answers:
        if m==3:
            m=1
        if n==6:
            n=1
        convert = 0
        if n == 1:
            convert = 3
        elif n== 2:
            convert = 1
        elif n== 3:
            convert = 2
        elif n== 4:
            convert = 4
        elif n==5:
            convert = 5
        if m == 1:
            p3.append(convert)
            m += 1
        elif m == 2:
            p3.append(convert)
            m += 1
            n += 1    
    players = [p1,p2,p3]
    for i in players:
        tmp = 0
        for x,y in zip(i,answers):
            if x == y:
                tmp += 1
        count.append(tmp)
    winner = max(count)
    answer = []

    for i in range(0,3):
        if winner == count[i]:
            answer.append(i+1)
    return answer


answers = [1,3,2,4,2]

solution(answers)