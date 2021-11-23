def solution(s):
    answer = []
    making_list = []
    t_condition = 0
    _t_condition = 0
    num_list = []
    numbers = ''
    for j in s:
        if t_condition == 1:
            if j.isdecimal():
                numbers = numbers + j
            elif j == ",":
                num_list.append(int(numbers))
                numbers = ''

        if j == "{":
            t_condition = 1

        if j == "}" and t_condition == 1:
            
            num_list.append(int(numbers))
            making_list.append(num_list)
            numbers = ''
            num_list = []
            t_condition = 0
    making_list.sort(key=len)
    for i in making_list:
        for j in i:
            if j in answer:
                pass
            else:
                answer.append(j)
    return answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
solution(s)