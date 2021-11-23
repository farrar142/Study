import random

matrix = []
row = int(input(""))
for i in range(row):
    matrix_sub = []
    for j in range(row):
        if random.randint(0,3)== 0:
            matrix_sub.append("*")
        else:
            matrix_sub.append(".")
    matrix.append(matrix_sub)

for i in range(len(matrix)):#y좌표
    for j in range(len(matrix)):#x좌표
        if matrix[i][j] ==".":
            count = 0
            for s_p in  [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                if row>i+s_p[0]>=0 and row>j+s_p[1]>=0:
                    if matrix[i+s_p[0]][j+s_p[1]] == "*":
                        count += 1
            matrix[i][j] = count
for i in matrix:
    for j in i:
        print(j,end=" ")
    print("")