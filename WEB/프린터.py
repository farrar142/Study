def solution(priorities, location):
    answer = 0    
    cur_doc = priorities[0]
    priorities.pop(0)
    printed = 0
    checker = 1
    while(priorities):
        if len(priorities) == 0:
            answer = printed +1
        if (checker == 0):
            if (location == 0):##높은 수가 없고, 목표하는 문서였을 경우
                answer = printed
                break
            else:
                cur_doc = priorities.pop(0)##대기열 맨 앞의 문서 == 현재 문서
                printed+=1
                location -= 1
        checker = 0
        for i in range(len(priorities)):
            if cur_doc < priorities[i]:#현재 문서보다 더 큰 중요도 문서가 있을시
                checker = 1             #체커 증가
                priorities.append(cur_doc)#대기열에 현재문서 추가
                cur_doc = priorities.pop(0)##대기열 맨 앞의 문서 == 현재 문서
                if location == 0:##목표 문서였을경우 맨뒤로밈
                    location = len(priorities)
                else:
                    location -= 1
    answer = printed + 1
    return answer

priorities = [1,1,1,1]
location = 3

print(solution(priorities,location))