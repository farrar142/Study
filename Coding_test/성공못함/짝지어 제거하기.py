
def solution_1(s):
    if len(s)%2==1:
        return 0
    s = list(s)    
    did_i = 1
    while did_i == 1:
        did_i = 0
        i = 0
        while (i < len(s)-1):
            if (i < len(s)):
                if s[i]==s[i+1]:
                    did_i = 1
                    s,i = pop_it(s,i)                    
            else:
                i+=1
                break
            i+=1
            #print(s,i,t)
    if len(s) >= 1:
        return 0
    else:
        return 1

def pop_it(list,index):
    #스택
    try:
        if list[index] == list[index+1]:
            del list[index:index+2]
            if index >= 1:
                pop_it(list,index-1)
            else:
                pop_it(list,index)
        else:
            return list,index
    except:
        return list,index
    return list,index



s = 'abccccbaaa'

import sys
sys.setrecursionlimit(1000000)


def solution(s):
    s = list(s)
    answer = stack(s,0)
    return answer

def stack(list,index):
    try:   
        if list[index] != list[index+1]:
            stack(list,index+1)#다음 인덱스 탐색

        elif list[index] == list[index+1]:
            del list[index:index+2]#현재인덱스와 다음인덱스요소 삭제

            if index >= 1:
                stack(list,index-1)#인덱스 -1 부터 탐색
            else:
                stack(list,index)#현재 인덱스 부터 탐색.
    except:
        pass#인덱스 오류시 스택쌓기 끝

    if len(list) == False:
        return 1
    elif len(list) >= 1:
        return 0

solution(s)