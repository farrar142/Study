class node:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type
    def show(self):
            return(self.type)

def solution(places):
    global matrix
    answer = []
    for i in range(len(places)):
        ##5x5배열당
        partial_answer = 1
        #좌표와 타입을 가지고 있는 클래스로된 2차원 배열
        matrix = []        
        for j in range(5):
            matrix_r = []
            for k in range(5):
                if places[i][j][k] == "P": 
                    matrix_r.append(node(j,k,"P"))
                elif places[i][j][k] == "O": 
                    matrix_r.append(node(j,k,"O"))
                elif places[i][j][k] == "X": 
                    matrix_r.append(node(j,k,"X"))
            matrix.append(matrix_r)
        for m in matrix:
            for n in m:
                print(n.type,end=" ")
            print()
        #응시자들만 추림
        participant = []
        for x in matrix:
            for y in x:
                if y.type == "P":
                    participant.append(y)

        for x in participant:
            for y in participant[participant.index(x)+1:]:
                m_d = abs(x.x-y.x)+abs(x.y-y.y)
                print(f"1 : {x.x},{x.y} ,2 : {y.x},{y.y}")
                print(f"type{matrix[x.y][y.x].type}")
                if m_d <= 1:
                    partial_answer = 0
                elif m_d ==2:
                    two_partition = matrix[x.x][y.y].type + matrix[y.x][x.y].type
                    if  two_partition == "XX":
                        pass
                    elif x.x == y.x:
                        if matrix[x.x][int(abs(x.y + y.y)/2)].type == "X":
                            pass
                        else:
                            partial_answer = 0
                    elif x.y == y.y:
                        print("here")
                        if matrix[int(abs(x.x + y.x)/2)][x.y].type == "X":
                            pass
                        else:
                            partial_answer = 0
                    else: 
                        print(two_partition)
                        print(f"1 : {x.x},{x.y} ,2 : {y.x},{y.y}")
                        print(f"type{matrix[x.y][y.x].type}")
                        partial_answer = 0                            
        answer.append(partial_answer)
    return answer


places = [[
    "OOOOO", 
    "OPOOO", 
    "OXOOO", 
    "OPOOO", 
    "OOOOO"]]


solution(places)