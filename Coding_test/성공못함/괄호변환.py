def solution(p):
    answer = ''

    if p == "":
        return answer
    if is_correct(p):
        return p
    splitter(p)
    return answer

def is_correct(p):
    _p = list(p)
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

def make_correct(p):
    if is_correct(p):
        return p
    else:
        return ''.join(list(reversed(p)))

def splitter(p):
    if len(p) == 0:
        return ""
    cur_c = p[0]
    checker = 1
    turned = 0
    for i_x,k_x in enumerate(p[1:]):
        if k_x == cur_c:
            if turned == 0:
                checker += 1
            else:
                if checker >= 1:
                    checker -= 1
                else:
                    return str(make_correct(p[:i_x+1])) + str(splitter(p[i_x+1:]))
        elif k_x != cur_c:
            if checker >= 1:
                cur_c = k_x
                turned = 1
                checker -= 1
            else:
                return str(make_correct(p[:i_x-1])) + str(splitter(p[i_x-1:]))
        elif (k_x != cur_c) and turned == 1:
            return [ ],[make_correct(p)]
        if checker == 0:
            return str(make_correct(p[:i_x+2])) + str(splitter(p[i_x+2:]))

p = ")("
solution(p)