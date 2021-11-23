



def solution(triangle):
    enum = enumerate
    t = triangle
    for index,i in enum(t):
        reset = []
        for ind,j in enum(i):
            reset.append([ind,j])
        t[index] = reset
        
    for i in range(1,len(t)):
        new = []
        for j in t[i-1]:
            for k in t[i]:
                if (k[0] - j[0]) in [0,1]:
                    new.append([k[0],k[1]+j[1]])
        t[i] = new
    
    t[-1].sort(key = lambda x:x[1])
    answer = t[-1][-1][1]
    
    
    
        
        
    
    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def try_sum(t):
    for index,i in enum(t):
        reset = []
        for ind,j in enum(i):
            reset.append([ind,j])
        t[index] = reset
        print(reset)
        
    for i in range(1,len(t)):
        new = []
        for j in t[i-1]:
            for k in t[i]:
                if (k[0] - j[0]) in [0,1]:
                    new.append([k[0],k[1]+j[1]])
        t[i] = new
        for m in t:
            print(m)






solution(triangle)

# p = index  c = index *2 , index *2 +1

