import random

maze = []
range_maze = 0
def make_maze():
    global maze,range_maze
    range_maze = random.randint(30,30)
    in_maze = []
    for i in range(0,range_maze):
        for j in range(0,range_maze):
            in_maze.append(0)
        maze.append(in_maze)
        in_maze = []
def make_barrier():
    global maze
    for i in range(0,len(maze)):
        for j in range(0,len(maze[i])):
            stand = random.randint(0,10)
            if stand >= 8:
                maze[i][j] = 1
            else:
                maze[i][j] = 0

class CO:
    black = '\033[30m'
    red = '\033[41m'
    green = '\033[32m'
    yellow = '\033[33m'
    white = '\033[97m'
    cyan = '\033[96m'
    RESET = '\033[0m'

def print_maze():
    for i in range(0,len(maze)):
        for j in range(0,len(maze[i])):
            if maze[i][j] == 1:
                print(CO.red + str(maze[i][j]), CO.RESET ,end=" ")
            elif maze[i][j] ==2:
                print(CO.yellow + str(maze[i][j]), CO.RESET ,end=" ")
            elif maze[i][j] == 3:
                print(CO.green + str(maze[i][j]), CO.RESET ,end=" ")
            elif maze[i][j] == 5:
                print(CO.cyan + str(maze[i][j]), CO.RESET ,end=" ")
            elif maze[i][j] >= 7:
                print(CO.white + str(maze[i][j]), CO.RESET ,end=" ")
            
            else:
                print(CO.black + str(maze[i][j]), CO.RESET ,end = " ")
        print("\n")


make_maze()
make_barrier()

class node:
    x = 0#좌표
    y = 0#좌표
    d = 0#거리
    def __init__(self,x,y,d = 0,parent = None):
        self.parent = parent
        self.path = (x,y)
        self.x = x
        self.y = y
        self.d = d

    def show_path(self):
        return(self.path)
        #print(self.parent)
    def p(self):
        return self.x,self.y



def start_find(a,b,c,d):
    def dist(ae,ad):
        return (ae - end_node.x)**2+(ad - end_node.y)**2
    maze[b][a] = 0
    maze[d][c] = 0
    distance = (c-a)**2+(d-b)**2
    start_node = node(b,a,distance)
    end_node = node(d,c)
    def start_end():
        maze[start_node.x][start_node.y] = 8
        maze[end_node.x][end_node.y] = 9
    print(distance,"거리")

    candidate_node = []
    candidate_node.append(start_node)
    already_node = []
    sequence = 0
    if maze[start_node.x][start_node.y] == 1:
        return "시작 지점에 장애물"

    if maze[end_node.x][end_node.y] == 1:
        return "목표 지점에 장애물"

    while candidate_node:# and sequence <= 3:
        
        current_node = candidate_node[0]#현재노드를 예상노드 1로 설정
        for item in candidate_node:
            if item.d < current_node.d:
                candidate_node.remove(item)
                candidate_node.insert(0,item)
                current_node = item
                print("더 가까운 노드로 수정")
        print(current_node.path[::-1],"현재위치")
        print(current_node.d,"예상 거리")

        if current_node.p() != end_node.p():
            for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:#,
                #(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                #새로운 예상노드 생성
                new_node = node(
                    current_node.x + newPosition[0],
                    current_node.y + newPosition[1],
                    dist(current_node.x + newPosition[0],
                    current_node.y + newPosition[1]),current_node)#자식노드에 현재노드를 부모로 넘겨줌
                #new_node.d = dist(new_node)

                within_range_criteria = [
                    new_node.x < 0,
                    new_node.x > (len(maze) - 1),
                    new_node.y < 0,
                    new_node.y > (len(maze[len(maze) - 1]) - 1)]

                if any(within_range_criteria):#새로운 노드가 메이즈 범위 밖,
                    continue
                if new_node.path in already_node:#새로운 노드가 이미 들른 노드에 있음
                    #print(new_node.p(),maze[new_node.x][new_node.y],"이미 들른 지점")
                    continue
                if maze[new_node.x][new_node.y] == 1:#새로운 노드에 장애물이 있음
                    #print(new_node.p(),maze[new_node.x][new_node.y],"장애물파악")
                    continue
                candidate_node.append(new_node)
                maze[new_node.x][new_node.y] = 2
                #print(new_node.p(),"추가된노드")

            maze[current_node.x][current_node.y] = 5 #현재지점 마킹
            already_node.append(current_node.path)
            candidate_node.pop(0) #현재지점을 예상지점에서 뺌

            # for i in candidate_node:
            #     print(i.p(),end = "")
            # print("찾아갈길")


        elif current_node.p() == end_node.p():
            print("골인")
            current_node.show_path()
            candidate_node = []
            path = []
            current = current_node
            while current is not None:
                path.append(current.show_path()[::-1])
                maze[current.path[0]][current.path[1]] = 3
                current = current.parent
            start_end()
            print_maze()
            print(sequence,"번의 시행")
            print(len(path),"거리")
            
            return path[::-1]  # reverse
        
        sequence += 1
        #print(sequence,"번의 시행")
            
    if candidate_node == []:
        start_end()
        print_maze()
        return "길이 막혀있습니다."
what_a = random.randint(0,range_maze-1)
what_b = random.randint(0,range_maze-1)
what_c = random.randint(0,range_maze-1)
what_d = random.randint(0,range_maze-1)


start_find(0,0,what_c,what_d)
#start_find(1,1,39,39)