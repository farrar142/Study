import random

class CO:
    black = '\033[30m'
    red = '\033[41m'
    green = '\033[32m'
    yellow = '\033[33m'
    white = '\033[97m'
    cyan = '\033[96m'
    RESET = '\033[0m'

class Node:
    x = 0
    y = 0
    def __init__(self,x,y,parent = None):
        self.x = x
        self.y = y
        self.path = (x,y)
        self.parent = parent

maze = []
range_maze = 0
def make_maze():
    global maze,range_maze
    range_maze = 9
    in_maze = []
    for i in range(0,31):
        for j in range(0,31):
            in_maze.append(0)
        maze.append(in_maze)
        in_maze = []
def make_barrier():
    global maze
    for i in range(0,len(maze)):
        if i % 2 == 1: # 홀수 행은 하나건너 가벽을 세움

            for j in range(0,len(maze[i]),2):
                if j == 0:
                    maze[i][j] = 1
                elif j == len(maze)-1:
                    maze[i][j] = 1 ## 벽은 장애물
                else:
                    maze[i][j] = 2 ## 중간은 가벽

            

        elif i % 2 ==0:#짝수행은 벽으로       

            for j in range(0,len(maze[i])):
                    maze[i][j] = 1

            if i > 1 and i < len(maze)-1:#미로의 시작과 끝은 처리 안함
                for j in range(0,len(maze[i])-1,2):#중간 가벽을 세움
                        maze[i][j+1] = 2

def delete_temp_barrier():
    global maze
    for i in range(0,len(maze)):
        for j in range(0,len(maze)):
            if maze[i][j] == 2:
                maze[i][j] = 1

def print_maze():
    # maze[29][28] = 0
    # maze[28][29] = 0
    for i in range(0,len(maze)):
        for j in range(0,len(maze[i])):
            if maze[i][j] == 1:
                print(CO.red + str(maze[i][j]), CO.RESET ,end=" ")
            elif maze[i][j] ==2:
                print(CO.red + str(maze[i][j]), CO.RESET ,end=" ")
                #print(CO.yellow + str(maze[i][j]), CO.RESET ,end=" ")
            elif maze[i][j] == 3:
                print(CO.green + str(maze[i][j]), CO.RESET ,end=" ")
            elif maze[i][j] == 5:
                print(CO.cyan + str(maze[i][j]), CO.RESET ,end=" ")
            elif maze[i][j] == 7:
                print(CO.red + str(maze[i][j]), CO.RESET ,end=" ")
            elif maze[i][j] >= 8:
                print(CO.white + str(maze[i][j]), CO.RESET ,end=" ")
            
            else:
                print(CO.black + str(maze[i][j]), CO.RESET ,end = " ")
        print("\n")

make_maze()
make_barrier()


def make_path():
    global maze ,current_Node,candidate_Node,child_expected_node
    start_Node = Node(1,1)
    end_Node = Node(29,29)
    def start_end():
        maze[start_Node.x][start_Node.y] = 8
        maze[end_Node.x][end_Node.y] = 9

    candidate_Node = []
    candidate_Node.append(start_Node)
    already_Node = []
    child_sequence = 0
    
    child_expected_node = []
    sequence = 0
    if maze[start_Node.x][start_Node.y] == 1:
        return "시작 지점에 장애물"

    if maze[end_Node.x][end_Node.y] == 1:
        return "목표 지점에 장애물"

    while candidate_Node:# and sequence <= 3:
        already_Node = list(set(already_Node))
        items_count = 0
        for items in candidate_Node:#already패쓰에 있는것들을 걸러냄
            if items.path in already_Node:
                candidate_Node.pop(items_count)
                items_count -= 1
            items_count += 1

        random.shuffle(candidate_Node)
        if candidate_Node:
            current_Node = candidate_Node[0]#현재노드를 예상노드 1로 설정
        else:
            return print_maze(),"1번"
        
        # print(current_Node.path[::-1],"현재위치")
        # print(current_Node.d,"예상 거리")

        if current_Node.path != end_Node.path:
            for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:#,
                #(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                #새로운 예상노드 생성
                new_Node = Node(
                    current_Node.x + newPosition[0],
                    current_Node.y + newPosition[1],
                    current_Node)#자식노드에 현재노드를 부모로 넘겨줌

                within_range_criteria = [
                    new_Node.x < 0,
                    new_Node.x > (len(maze) - 1),
                    new_Node.y < 0,
                    new_Node.y > (len(maze[len(maze) - 1]) - 1)]

                if any(within_range_criteria):#새로운 노드가 메이즈 범위 밖,
                    continue
                if new_Node.path in already_Node:#새로운 노드가 이미 들른 노드에 있음
                    continue
                if maze[new_Node.x][new_Node.y] == 1:#새로운 노드에 장애물이 있음
                    continue
                candidate_Node.append(new_Node)
                maze[new_Node.x][new_Node.y] = 3
                #print(new_Node.p(),"추가된노드")

            if current_Node.path not in already_Node:
                maze[current_Node.x][current_Node.y] = 5 #현재지점 마킹

            already_Node.append(current_Node.path)
            if candidate_Node:
                candidate_Node.pop(0) #현재지점을 예상지점에서 뺌
            else:
                return print_maze,"2번"
            if candidate_Node:
                current_Node = candidate_Node[0]#현재 노드 초기화
            else:
                return print_maze , "2번 다음"
            child_expected_node.append(candidate_Node[0])#자식들에게 초기값을 넘겨줌




        child_sequence = 0
        while child_expected_node and child_sequence < 4:                
            already_Node = list(set(already_Node))#얼레디노드 디버깅용
            items_count = 0
            for items in child_expected_node:#already패쓰에 있는것들을 걸러냄
                if items.path in already_Node:
                    child_expected_node.pop(items_count)
                    items_count -= 1
                items_count += 1

            if child_expected_node:
                child_current_Node = child_expected_node[0]
                if (child_current_Node.path in already_Node):
                    if len(child_expected_node) > 1:
                        child_expected_node.pop(0)
                        child_current_Node = child_expected_node[0]
            else:
                return print_maze(),"3번"

            if child_current_Node.path != end_Node.path:
                for child_newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:#,
                    #(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    #새로운 예상노드 생성
                    new_Node = Node(
                        child_current_Node.x + child_newPosition[0],
                        child_current_Node.y + child_newPosition[1],
                        child_current_Node)#자식노드에 현재노드를 부모로 넘겨줌

                    within_range_criteria = [
                        new_Node.x < 0,
                        new_Node.x > (len(maze) - 1),
                        new_Node.y < 0,
                        new_Node.y > (len(maze[len(maze) - 1]) - 1)]

                    if any(within_range_criteria):#새로운 노드가 메이즈 범위 밖,
                        continue
                    if new_Node.path in already_Node:#새로운 노드가 이미 들른 노드에 있음
                        continue
                    if maze[new_Node.x][new_Node.y] == 1:#새로운 노드에 장애물이 있음
                        continue
                    child_expected_node.append(new_Node)
                    candidate_Node.append(new_Node)
                    #maze[new_Node.x][new_Node.y] = 4
                    #print(new_Node.p(),"추가된노드")

                if child_current_Node.path not in already_Node:
                    maze[child_current_Node.x][child_current_Node.y] = 6 #현재지점 마킹

                already_Node.append(child_current_Node.path)#현재 지점을 얼레디에 넣음
            child_expected_node.pop(0) #현재지점을 예상지점에서 뺌
            candidate_Node.pop(0) # 현재지점을 부모노드에서 뺌
            child_sequence += 1       
            if candidate_Node:
                current_Node = candidate_Node[0]#현재 노드 초기화
            else:
                return print_maze()
            
            
            # if child_current_Node.path == end_Node.path:
            #     candidate_Node = []
            #     start_end()
            #     #delete_temp_barrier()
            #     print_maze()
            #     return "끗"

        #child_current_Node = child_current_Node.parent
        maze[child_current_Node.x][child_current_Node.y] = 7 # 막다른길


        # if current_Node.path == end_Node.path:
        #     candidate_Node = []
        #     path = []
        #     current = current_Node
        #     start_end()
        #     #delete_temp_barrier()
        #     print_maze()
        #     return "끗"
        
        sequence += 1
        #print(sequence,"번의 시행")
            
    if candidate_Node == []:
        start_end()
        delete_temp_barrier()
        print_maze()
        return "길이 막혀있습니다."
    

make_path()