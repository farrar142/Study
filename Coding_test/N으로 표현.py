N = 5
number = 12


def solution(N, number):
    array = [[0]]
    for i in range(1,9):
        array.append([int(str(N)*i)])
    for i in array:
        if i[0]==number:
            return array.index(i)
    
    for i in range(2,9):#i 번째 계산
        for j in range(1,i): #계산된 리스트에 대해
            for a in array[j]:#2
                for b in array[i-j]:#3
                    array[i].append(a+b)
                    array[i].append(a-b)
                    array[i].append(a*b)
                    if b != 0:
                        array[i].append(a/b)
                        
        if number in array[i]:
            return i
        array[i] = list(set(array[i]))
    
    
    return -1



solution(N,number)