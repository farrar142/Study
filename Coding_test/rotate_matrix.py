def solution(rows, columns, queries):

    matrix = []
    answer = []
    x = 1
    for i in range(0,rows):
        matrix_a = []
        for j in range(0,columns):
            matrix_a.append(x)
            x += 1
        matrix.append(matrix_a)
    
    for i in queries:
        coord_list = []
        value_list = []
        x1 = i[0]-1
        y1 = i[1]-1
        x2 = i[2]-1
        y2 = i[3]-1

        ##좌표값과 저장된값 저장.
        for y1_y2 in range(y1,y2+1):
            value_list.append(matrix[x1][y1_y2])
            coord_list.append([x1,y1_y2])
        value_list.pop(-1)
        coord_list.pop(-1)
        for x1_x2 in range(x1,x2+1):
            value_list.append(matrix[x1_x2][y2])
            coord_list.append([x1_x2,y2])
        value_list.pop(-1)
        coord_list.pop(-1)
        for y1_y2 in range(y2,y1-1,-1):
            value_list.append(matrix[x2][y1_y2])
            coord_list.append([x2,y1_y2])
        value_list.pop(-1)
        coord_list.pop(-1)
        for x1_x2 in range(x2,x1-1,-1):
            value_list.append(matrix[x1_x2][y1])
            coord_list.append([x1_x2,y1])
        value_list.pop(-1)
        coord_list.pop(-1)

        value_list.insert(0,value_list.pop(-1))

        for index,value in enumerate(coord_list):
            matrix[value[0]][value[1]] = value_list[index]
        answer.append(min(value_list))
    return answer




row = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution (row, columns,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])
