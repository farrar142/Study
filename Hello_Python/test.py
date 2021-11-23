import random
import Terrain_Generate
from Terrain_Generate import Node

def make_terrain_route(self,terrain_type = "pln",node_depth=20,node_tendency=2):
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
            for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:#,
            #(-1, -1), (-1, 1), (1, -1), (1, 1)]:
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
                if self.map[self.new_node.x][self.new_node.y] != "pln":#새로운 노드에 장애물이 있음
                    continue
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

            if self.node_should_i_continue == False:
                if random.randint(0,node_tendency) <= 0:
                    self.node_fluid_expected = [random.choice(self.node_fluid_expected)]#찾아갈 경로에 예상경로중 하나만 남겨둠
                    
                    
                    #찾아갈 경로에 예상경로중 제일 가까운 경로를 추가
                else :
                    for item in self.node_fluid_expected:#예상 경로에서
                        if item.path == self.node_end_node.path:
                            self.node_current_node = item
                            self.node_fluid_expected = [item]
                        elif item.d < self.node_current_node.d: # 아이템의 디스턴스들을 검색
                            self.node_fluid_expected.remove(item)
                            self.node_fluid_expected.insert(0,item)
                            self.node_current_nodecurrent_node = item
                    self.node_fluid_expected = [self.node_fluid_expected[0]]#경로를 하나만 남겨둠
                            #print("더 가까운 노드로 수정")



        else:#예상경로가 남아있지 않을시
            self.current_coord = self.node_current_node
            self.path = []

            while self.current_coord is not None:
                self.path.append(self.current_coord.path[::-1])
                self.map[self.current_coord.path[0]][self.current_coord.path[1]].type = terrain_type                    
                self.map[self.current_coord.path[0]][self.current_coord.path[1]].height = self.current_coord.h#여태까지 경로들에 부모의 높이값 추가
                if self.map[self.current_coord.path[0]][self.current_coord.path[1]].height <= 0:                            
                    self.map[self.current_coord.path[0]][self.current_coord.path[1]].type = "pln"  
                self.current_coord = self.current_coord.parent##여태 까지의 경로들을 물로 지정
            #self.end_node.type = "pln"
            #self.end_node.height = 0
            #return self.path[::-1]#, print("탐색이 목표까지 도달하지 못함")

    fluid_sim(Current_Map,-70,"node")