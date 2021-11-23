def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(0,len(speeds)):
            progresses[i] = progresses[i] + speeds[i]
        if progresses[0] >= 100:
            simultaneous = 0
            while progresses and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                simultaneous += 1
            answer.append(simultaneous)
    return answer

def solution_1(progresses, speeds):
    answer = []

    for i,j in zip(progresses,speeds):
        day = -((i-100)//j)
        if len(answer)==0 or answer[-1][0]<day:
            answer.append([day,1])
        else:
            answer[-1][1]+=1
    return [q[1] for q in answer]



progresses = [93, 30, 55]
speeds = [1,30,5]

solution_1(progresses,speeds)