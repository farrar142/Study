import heapq as hq
def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)##힙 생성
    while (True):
        cur_num = hq.heappop(scoville)
        if cur_num >= K:
            return answer
        if len(scoville)==0:
            return -1
        next_num = hq.heappop(scoville)#그 다음으로 작은 원소
        hq.heappush(scoville,(cur_num + (next_num*2)))
        answer += 1


    
scoville = [3,25,322,6223,66623,2245]
K = 90000
solution(scoville,K)
