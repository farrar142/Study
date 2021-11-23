absolutes = [4,7,12]
signs = [true,false,true]
print(type(signs[0]))
def solution(absolutes, signs):
    sum = 0
    for x,y in zip(absolutes,signs):
        if y == true:
            sum +=x
        else:
            sum -= x
    print(sum)
    return

#solution(absolutes,signs)