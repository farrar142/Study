N = 4

stages =[4,4,4,4,4]

def solution(N,stages):
    whos_in = []
    for j in range(0,N+1):
        whos_in.append(0)
    for i in stages:
        for j in range(0,i):
            whos_in[j] += 1
    rate = []
    for i in range(0,len(whos_in)-1):
        try:
            rate.append((whos_in[i] - whos_in[i+1])/whos_in[i])
        except:
            rate.append(0)
    rate_dict = {}
    for index,item in enumerate(rate):
        rate_dict[index+1] = item
    rate_dict = sorted(rate_dict.items())
    #print(rate_dict)
    for i in range(0,len(rate_dict)-1):
        for j in range(i,len(rate_dict)):
            #print(rate_dict)
            prev = rate_dict[i][1]
            next = rate_dict[j][1]
            if prev < next:
                rate_dict.insert(j,rate_dict.pop(i))
                rate_dict.insert(i,rate_dict.pop(j-1))
            elif prev == next:
                if rate_dict[i][0] > rate_dict[j][0]:
                    rate_dict.insert(j,rate_dict.pop(i))
                    rate_dict.insert(i,rate_dict.pop(j-1))

    return [i[0] for i in rate_dict]


solution(N,stages)