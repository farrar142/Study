import random
from typing import Mapping

class CO:
    black = '\033[30m'
    green_b = '\033[42m'
    green_d = '\033[32m'
    green_y = '\033[92m'
    yellow = '\033[33m'
    white = '\033[97m'
    blue_b = "\033[104m"
    blue_d = '\033[34m'
    blue_y = '\033[94m'
    cyan_b = "\033[106m"
    cyan_d = '\033[36m'
    cyan_y = '\033[96m'
    RESET = '\033[0m'


class Terrain:
    x = 0
    y = 0
    coord = []
    height = 0
    type = ""
    parent = []

    def __init__ (self,x,y,height=0,type = "pln"):
        self.x = x
        self.y = y
        self.coord = x,y
        self.height = height
        self.type = type
        
class Node:
    x = 0#좌표
    y = 0#좌표
    h = 0#높이
    #d = 0#거리
    def __init__(self,x,y,d=0,h=0,parent = None):
        self.parent = parent
        self.path = (x,y)
        self.x = x
        self.y = y
        self.h = h
        self.d = d

    def show_path(self):
        return(self.path)
        #print(self.parent)
    def p(self):
        return self.x,self.y

class Map:
    map = []
    x_length = 0
    y_length = 0
    aspect = []

    def __init__ (self,x,y,z):
        self.x_length = x
        self.y_length = y
        self.z_length = z

        for x_p in range(0,x):
            self.map_x = []
            for y_p in range(0,x):
                self.map_x.append(Terrain(x_p,y_p))
            self.map.append(self.map_x)

        for x_p in range(0,z):
            self.map_z = []
            for y_p in range(0,x):
                self.map_z.append(" ")
            self.aspect.append(self.map_z)

    def show_height(self):
        for i in self.map:
            for ite in i:
                print(str(ite.height).rjust(3),end=",")
            print("\n")

    def show_coord(self):
        for i in self.map:
            for ite in i:
                print(str(str(ite.x)+"."+str(ite.y)).rjust(5),end=",")
            print("\n")

    def show_type(self):
        for i in self.map:
            for ite in i:
                if ite.type == "pln":
                    print(CO.green_y + str(ite.type).rjust(3),CO.RESET,end="")
                elif ite.type == "wtr":
                    if ite.height > -5:                    
                        print(CO.cyan_b + CO.white + str(ite.type).rjust(3),CO.RESET,end="")
                    elif ite.height >= -9:                    
                        print(CO.cyan_b + CO.white + str(ite.type).rjust(3),CO.RESET,end="")
                    elif ite.height >= -15:                    
                        print(CO.blue_b + CO.black + str(ite.type).rjust(3),CO.RESET,end="")
                    else:                    
                        print(CO.blue_b + CO.black + str(ite.type).rjust(3),CO.RESET,end="")
                
                elif ite.type == "hil":
                    print(CO.yellow+ str(ite.type).rjust(3),CO.RESET,end="")
                
                elif ite.type =="mtn":           
                    if ite.height >10:
                        print(CO.green_b+CO.black + str(ite.type).rjust(3),CO.RESET,end="")
                    else:
                        print(CO.green_b+CO.white + str(ite.type).rjust(3),CO.RESET,end="")
                elif ite.type == "rod":
                    print(CO.black+ str(ite.type).rjust(3),CO.RESET,end="")
                
                elif ite.type in ["brg","tnl"]:
                    print(CO.black+ str(ite.type).rjust(3),CO.RESET,end="")

                else:
                    print(str(ite.type).rjust(3),end=" ")
            print("")        
            for ite in i:
                if ite.height != 0:
                    print(str(ite.height).rjust(3),end=" ")
                else:
                    print(str("").rjust(3),end=" ")
            print("")

    def show_aspect_x(self):
        for k in self.map:#맵x좌표중의
           for i in k:#x.y에 대해
        #for i in self.map[0]:#x.y에 대해
            if i.height >= 0:
                for j in range(0,i.height):
                    self.aspect[j][i.y] = "X"
        self.aspect.reverse()


        for i in self.aspect:
            for ite in i:
                print(ite.rjust(3),end=" ")    
            print("")
        print("")
        self.aspect.reverse()

        for i in range(0,len(self.aspect)):
            for j in range(0,len(self.aspect[0])):
                self.aspect[i][j] = " "

    def show_aspect_y(self):
        for k in self.map:#맵x좌표중의
           for i in k:#x.y에 대해
        #for i in self.map[0]:#x.y에 대해
            if i.height >= 0:
                for j in range(0,i.height):
                    self.aspect[j][i.x] = "Y"
        self.aspect.reverse()


        for i in self.aspect:
            for ite in i:
                print(ite.rjust(3),end=" ")    
            print("")
        print("")
        self.aspect.reverse()

        for i in range(0,len(self.aspect)):
            for j in range(0,len(self.aspect[0])):
                self.aspect[i][j] = " "
        


def fluid_sim(index,slope,Type):
    global Terrain,Map,fluid_already
    if slope > 0:
        slope_random_range = 0,slope
    if slope <= 0:
        slope_random_range = slope,0
    fluid_list = []
    fluid_already = []
    #초기 세팅
    for i in range(0,len(index.map)-1):
        for j in range(0,len(index.map)-1):
            #타입이 일치하고,들르지 않았고, 설정해둔 값보다 높은값이 있을시
            if index.map[i][j].coord not in fluid_already:
                if (index.map[i][j].type == str(Type)):
                    if(abs(index.map[i][j].height) >= 0):
                        fluid_list.append(index.map[i][j])
                        fluid_already.append(index.map[i][j].coord)
                        #print("검색완료")

                        
    while fluid_list:#슬로프값보다 높은 리스트가 있을시
        current_fluid = fluid_list[0]#리스트의 첫번째값에서 부모를 생성
        #print(type(current_fluid))

        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0),(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            #새로운 예상노드 생성
            new_node = Terrain(
                current_fluid.x + newPosition[0],
                current_fluid.y + newPosition[1],
                current_fluid.height + random.randint(slope_random_range[0],slope_random_range[1]),#현재트레인에 추가된 높이값
                Type)
            within_range_criteria = [
                new_node.x < 0,
                new_node.x > (len(index.map) - 1),
                new_node.y < 0,
                new_node.y > (len(index.map[len(index.map) - 1]) - 1)]

            if any(within_range_criteria):#새로운 트레인이 맵 범위 밖,
                continue
            if new_node.coord in fluid_already:#새로운 트레인이 이미 들른 트레인에 있음
                continue
            if slope >= 0 :
                if new_node.height >= 0:#새로운 트레인보다 현재트레인이 슬로프가 높음
                    fluid_already.append(new_node.coord)
                    continue
            if slope < 0 :
                if new_node.height <= 0:#새로운 트레인보다 현재트레인이 슬로프가 높음
                    fluid_already.append(new_node.coord)
                    continue
            if index.map[new_node.x][new_node.y].type != "pln":
                continue

            fluid_list.append(new_node)#예상노드에 새트레인 추가
            fluid_already.append(new_node.coord)

        fluid_list.pop(0)
        if index.map[current_fluid.x][current_fluid.y].type == "pln":#평지일때만 덮어씌우기
            index.map[current_fluid.x][current_fluid.y].type = current_fluid.type
            index.map[current_fluid.x][current_fluid.y].height = current_fluid.height
    
def make_terrain_route(self,terrain_type = "pln",node_depth=20,slope=20,node_tendency=2):
    global Terrain,Map

    def dist(x1,y1):
        return (x1 - self.end_node.x)**2+(y1 - self.end_node.y)**2

    self.up_or_left = ["up","left"]
    random.shuffle(self.up_or_left)

    if self.up_or_left[0] == "up":#시작을 위에서
        self.start_node = random.randint(0,len(self.map[0])-1)#위쪽의 랜덤한 좌표
        self.start_node = self.map[0][self.start_node]
        self.start_node.type = terrain_type
        self.start_node.height += random.randint(node_depth-1,node_depth)

        self.end_node = random.randint(0,len(self.map[0])-1)#아래쪽의 랜덤한 좌표
        self.end_node = self.map[len(self.map)-1][self.end_node]
        self.end_node.type = terrain_type
        self.end_node.height += random.randint(node_depth-1,node_depth)

    elif self.up_or_left[0] == "left":#시작을 왼쪽에서
        self.start_node = random.randint(0,len(self.map[0])-1)#왼쪽의 랜덤한 좌표
        self.start_node = self.map[self.start_node][0]
        self.start_node.type = terrain_type
        self.start_node.height += random.randint(node_depth-1,node_depth)

        self.end_node = random.randint(0,len(self.map[0])-1)#오른쪽의 랜덤한 좌표
        self.end_node = self.map[self.end_node][len(self.map)-1]
        self.end_node.type = terrain_type
        self.end_node.height += random.randint(node_depth-1,node_depth)

    self.node_start_node = Node(self.start_node.coord[0], self.start_node.coord[1],0,self.start_node.height )#스타트노드지정
    self.node_end_node = Node(self.end_node.coord[0],self.end_node.coord[1],0,self.start_node.height )#엔드노드 지정

    self.node_fluid_expected = []#예상지점 리스트 초기화
    self.node_fluid_expected.append(self.node_start_node)#예상지점에 현재노드를 넣음
    self.node_already_node = []#들른지점 리스트 초기화

    while self.node_fluid_expected:#예상지점이 있을시에

        self.node_current_node = self.node_fluid_expected[0]#현재 노드는 예상지점의 첫번째 노드

        if self.node_current_node.path != self.node_end_node.path:#현재노드가 도착지점이 아닐시
            for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:#,(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            #새로운 예상노드 생성
                self.new_node = Node(
                    self.node_current_node.x + newPosition[0],
                    self.node_current_node.y + newPosition[1],
                    dist(self.node_current_node.x + newPosition[0],
                        self.node_current_node.y + newPosition[1]),
                    self.node_current_node.h + random.randint(-1,1),#현재노드에 추가된 높이값
                    self.node_current_node)#자식노드에 현재노드를 부모로 넘겨줌

                within_range_criteria = [
                    self.new_node.x < 0,
                    self.new_node.x > (len(self.map) - 1),
                    self.new_node.y < 0,
                    self.new_node.y > (len(self.map[len(self.map) - 1]) - 1)]

                if any(within_range_criteria):#새로운 노드가 맵 범위 밖,
                    continue
                if self.new_node.path in self.node_already_node:#새로운 노드가 이미 들른 노드에 있음
                    continue
                # if self.map[self.new_node.x][self.new_node.y].type != "pln":#새로운 노드에 장애물이 있음
                #     continue
                self.node_fluid_expected.append(self.new_node)#예상노드에 새노드 추가

        #뉴노드 생성이 끝남
        self.node_already_node.append(self.node_current_node.path)
        #현재 경로의 좌표를 이미들른지점에 추가
        self.node_fluid_expected.pop(0)
        self.node_should_i_continue = False
        if self.node_fluid_expected:#예상경로가 남아있을시 
            for item in self.node_fluid_expected:#예상 경로에서
                    if item.path == self.node_end_node.path:
                        self.node_current_node = item
                        self.node_fluid_expected = [item]
                        #print('목표경로에 도착지점이있음')
                        self.node_should_i_continue = True

            if self.node_should_i_continue == False:#텐던시/목적지체크
                if random.randint(0,node_tendency) <= 0:
                    self.node_fluid_expected = [random.choice(self.node_fluid_expected)]#찾아갈 경로에 예상경로중 하나만 남겨둠
                    
                    
                    #찾아갈 경로에 예상경로중 제일 가까운 경로를 추가
                else :
                    for item in self.node_fluid_expected:#예상 경로에서
                        if item.path == self.node_end_node.path:#예상경로에 목적지가있음
                            self.node_current_node = item
                            self.node_fluid_expected = [item]
                        elif item.d < self.node_current_node.d: # 아이템의 디스턴스들을 검색
                            self.node_fluid_expected.remove(item)
                            self.node_fluid_expected.insert(0,item)
                            self.node_current_node = item
                    self.node_fluid_expected = [self.node_fluid_expected[0]]#경로를 하나만 남겨둠
                            #print("더 가까운 노드로 수정")



        else:#예상경로가 남아있지 않을시
            self.current_coord = self.node_current_node
            self.path = []

            while self.current_coord is not None:
                self.path.append(self.current_coord.path[::-1])
                if terrain_type == "rod":#길인경우 높이정보는 받지 않음
                    if self.map[self.current_coord.path[0]][self.current_coord.path[1]].type == "wtr" :#물인경우 브릿지                       
                        self.map[self.current_coord.path[0]][self.current_coord.path[1]].type = "brg"
                        self.map[self.current_coord.path[0]][self.current_coord.path[1]].parent = self.node_current_node 

                    
                    elif self.map[self.current_coord.path[0]][self.current_coord.path[1]].type in ["mtn","hil"] :#산인경우 터널                       
                        self.map[self.current_coord.path[0]][self.current_coord.path[1]].type = "tnl"
                        self.map[self.current_coord.path[0]][self.current_coord.path[1]].parent = self.node_current_node    

                    else:# self.map[self.current_coord.path[0]][self.current_coord.path[1]].type != "wtr":#물이아닌경우에 안받음
                        self.map[self.current_coord.path[0]][self.current_coord.path[1]].type = terrain_type 
                        self.map[self.current_coord.path[0]][self.current_coord.path[1]].parent = self.node_current_node

                elif self.map[self.current_coord.path[0]][self.current_coord.path[1]].type == "pln":#평지인 경우에만 지형 생성
                    if terrain_type != "rod":    
                        self.map[self.current_coord.path[0]][self.current_coord.path[1]].type = terrain_type                    
                        self.map[self.current_coord.path[0]][self.current_coord.path[1]].height = self.current_coord.h#여태까지 경로들에 부모의 높이값 추가
                        self.map[self.current_coord.path[0]][self.current_coord.path[1]].parent = self.node_current_node
                
                
                if node_depth < 0 and terrain_type == "wtr":#기준이 지하일때
                    if self.map[self.current_coord.path[0]][self.current_coord.path[1]].height >= 0:                            
                        self.map[self.current_coord.path[0]][self.current_coord.path[1]].type = "pln"  
                self.current_coord = self.current_coord.parent##여태 까지의 경로들을 물로 지정

    if self.node_current_node.path != self.end_node.coord:#도착하지 않았을때,
        self.map[self.end_node.coord[0]][self.end_node.coord[1]].type = "pln"
        self.map[self.end_node.coord[0]][self.end_node.coord[1]].height = 0
        print("d")
    if terrain_type != "rod":#길이 아닐시 fluid_sim실행
        fluid_sim(Current_Map,slope,terrain_type)


def make_terrain_hill(self,mtn_height=100,tendency=-100,mtn_number=1):
    global Terrain,Mapping
    
    while mtn_number >= 1:
        mtn_expected_list = []
        for mtn_x in self.map:
            for items in mtn_x:
                if items.type == "pln":
                    mtn_expected_list.append(items)
        mtn_expected_list=random.choice(mtn_expected_list)
        mtn_expected_list.type = "hil"
        mtn_expected_list.height = mtn_height
        mtn_number -= 1
    #print(mtn_expected_list)
    fluid_sim(Current_Map,tendency,"hil")
    
    pass


Current_Map = Map(30,30,50)
make_terrain_route(Current_Map,"wtr",-10,10,5)#대상맵,타입,높이or깊이,슬로프,텐던시
make_terrain_route(Current_Map,"mtn",20,-10,1)
make_terrain_route(Current_Map,"rod",0,0,2)
make_terrain_hill(Current_Map,10,-10,3)#높이,경사,갯수
Current_Map.show_aspect_y()
Current_Map.show_aspect_x()
#Current_Map.show_height()
Current_Map.show_type()
