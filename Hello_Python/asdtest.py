




class Head(Human_Body):
    def __init__(self,name,status = "Normal"):
        self.name = name
        self.right_eye = [100,status]
        self.left_eye = [100,status]
        self.right_ear = [100,status]
        self.left_ear = [100,status]
        self.nose = [100,status]
    def __repr__(self):
        return self.name+"'s "+self.__class__.__name__

class Human_Body:
    ##Head
    def __init__(self,name):
        self.name = name
        self.head = Head(name)
    def __repr__(self):
        return self.name

level_experience_table = []

level_table = []
experience_table = 10
for i in range(0,100):
    level_table.append((i+1,int(experience_table)))
    experience_table += experience_table/8
for i in level_table:
    print(i)

player_level = 1
player_experience = 20000

while level_table[player_level][1]<player_experience:
    player_experience -= level_table[player_level][1]
    player_level += 1
    print("Level up + 1 ,현재 레벨",player_level,"\n              현재 경험치",player_experience)