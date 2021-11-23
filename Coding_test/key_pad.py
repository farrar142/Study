numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]

def solution(numbers,hand):
    global array
    array = []
    i = 1
    for x in range(0,4):
        array_x = []
        for y in range(0,3):
            array_x.append(i)
            i += 1
        array.append(array_x)
    array[3][1] = 0;
    print(array)
    hand = hand
    left_xy = [3,0]
    right_xy = [3,2]
    cur_xy = [0,0]
    result = ""
    for num in numbers:
        if num in [1,4,7]:
            left_xy=get_xy(num)
            result= result + "L"
        elif num in [3,6,9]:
            right_xy=get_xy(num)
            result= result + "R"
        else:
            cur_xy = get_xy(num)
            if pyta(left_xy,cur_xy) < pyta(right_xy,cur_xy):
                left_xy=get_xy(num)
                result= result + "L"
            elif pyta(left_xy,cur_xy) > pyta(right_xy,cur_xy):
                right_xy=get_xy(num)
                result= result + "R"
            else:
                if hand == "right":
                    right_xy=get_xy(num)
                    result= result + "R"
                else:
                    left_xy=get_xy(num)
                    result= result + "L"
    answer = result
    return answer
def get_xy(num):
    for x in range(0,4):
        for y in range(0,3):
            if array[x][y] == num:
                return x,y
def pyta(arr0,arr1):
    cal = abs((arr0[0]) - arr1[0]) + abs(arr0[1] - arr1[1])
    return cal

            


solution(numbers,"left")