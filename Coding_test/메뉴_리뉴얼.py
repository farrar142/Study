def solution(orders, course):
    answer = []
    possible_list = []
    counter_list = []
    for menus in orders:
        if len(menus)>=2:
            for combi in course:
                for i in combination(menus,combi):
                    i.sort()
                    if i in possible_list:
                        counter_list[possible_list.index(i)] += 1
                    else:
                        possible_list.append(i)
                        counter_list.append(1)

    for length in course:
        cur_list = []
        cur_num = 0
        for items in possible_list:
            if len(items) == length:
                how_many = counter_list[possible_list.index(items)]
                if how_many > cur_num:
                    cur_list = []
                    cur_num = how_many
                    cur_list.append(items)
                elif how_many == cur_num:
                    cur_list.append(items)
        if cur_num >= 2:
            for i in cur_list:
                answer.append(''.join(i))
    answer.sort()
    return answer

def combination(strings,combi):
    result = []
    if len(strings) < combi:
        return result#길이보다 조합의 숫자가 길면 null
    else:
        for i in range(len(strings)):
            if combi == 1:
                yield [strings[i]]
            else:
                for next in combination(strings[i+1:], combi-1):
                    yield [strings[i]] + next


orders = 	["XYZ", "XWY", "WXA"]	
course = [2,3,4]

solution(orders, course) 