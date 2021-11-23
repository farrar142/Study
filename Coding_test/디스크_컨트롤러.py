def solution(jobs):
    answer = 0
    now_time = 0
    factor = len(jobs)
    next_jobs,now_time = get_next_jobs(jobs,now_time)
    while(next_jobs):
        cur_jobs = next_jobs.pop(0)#현재 작업 진행중
        jobs.remove(cur_jobs)
        ##현재작업시간 + 완료시까지 요청된 작업들을 검색해야됨
        now_time += cur_jobs[1]#현재 작업이 끝나면 시간이 증가함.
        answer += now_time - cur_jobs[0] #작업
        next_jobs,now_time = get_next_jobs(jobs,now_time)                
    answer = int(answer/factor)
    return answer
def get_next_jobs(a,now_time):
    result = []
    for i in a:
        if i[0] <= now_time:
            result.append(i)
    if (not result) and a:#작업이 다끝났지만 다음 작업이 한참 뒤에 있을 때
        a.sort(key = lambda x: x[0])
        for i in a:
            if i[0] == a[0][0]:##동일한 시간에 요청이 여럿 있을 때
                result.append(i)
        now_time = a[0][0]             
    result.sort(key = lambda x: x[1])
    return result,now_time
            



jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
solution(jobs)