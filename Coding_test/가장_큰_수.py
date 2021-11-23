def solution(numbers):
    answer=""
    numberStr=[]
    for i,value in enumerate(numbers):
        st = str(value)
        stri = st*3
        numberStr.append([stri,i])

    numberStr.sort(reverse=True)
    for i,value in enumerate(numberStr):
        index = value[1]
        answer += str(numbers[index])


    for value in answer:
        if value!='0':
            return answer

    return "0"
numbers = [3, 34, 30,31, 5, 9]
solution(numbers)
#자릿수비교  3,30,31,32,33,34


