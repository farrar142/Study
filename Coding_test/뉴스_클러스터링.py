def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    if str1 == str2:
        return 65536
    str1 = combination(str1)
    str2 = combination(str2)
    uni = union(str1,str2)
    compl = complement(str1,str2,uni)
    try:
        answer = int(len(uni)/len(compl) * 65536)
    except:
        answer = 0
    return answer

def combination(strings):
    result = []
    for i in range(0,len(strings)-1):
        cur_str = strings[i]+strings[i+1]
        checker = 0
        for i in cur_str:
            if i.isalpha():
                checker += 1
        if checker == 2:
            result.append(cur_str)
    result = sorted(result)        
    return result

def union(strings1,strings2):
    _str1 = list(strings1)
    _str2 = list(strings2)
    union = []

    for i in range(len(_str1)):
        for j in range(len(_str2)):
            if (_str1[i] == _str2[j]) and (_str1[i] != ""):
                union.append(_str1[i])
                _str1[i] = ""
                _str2[j] = ""
    return union

def complement(str1,str2,union):
    complement = sorted(str1+str2)
    for i in union:
        if i in complement:
            complement.pop(complement.index(i))    
    return complement
    

str1 = "A"
str2 = "aa1"
solution(str1,str2)