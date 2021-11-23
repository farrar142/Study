def solution(p):
    answer = ''
    if p == "":
        return ""
    print(splitter(p))
    return



def splitter(p):
    p = list(p)
    l = 0
    r = 0
    for index,item in enumerate(p):
        if item == "(":
            l += 1
        elif item == ")":
            r += 1
        if (l == r) and ((l+r) > 1):
            u = p[:index+1]
            v = p[index+1:]
            if is_correct(u):
                return u,v
            else:
                empty = ["("]
                empty = empty + splitter(v) + [")"]
                


def is_correct(p):
    _p = list(p)
    print(len(_p))
    for i in range(len(_p)-1):
        for j in range(i+1,len(_p)):
            l = _p[i]
            r = _p[j]
            if l == "c":
                break
            elif (l == "(") and (r == ")"):
                _p[i] = "c"
                _p[j] = "c"
    if ("("  in _p) or (")" in _p):
        return False
    else:
        return True
p = ")("
solution(p)