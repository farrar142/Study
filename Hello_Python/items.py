d_ma = {'wood':(10,0),'stone':(30,90),'iron':(40,95),'steel':(50,99)} # 기본값,내열성
d_qt = {'awful':0.9,'poor':0.95,'normal':1,'good':1.05,'excellent':1.1,'masterwork':1.15,'legendary':1.2}
d_me = {'early':0.9,'contemp':0.95,'nowday':1,'post':1.05,'futuristic':1.1}


class item():
    def __init__(self,name,material,quality,method,durability):
        self.Name = name
        self.Material = material
        self.Quality = quality
        self.Method = method
        self.Durability = durability
        self.blockage = d_ma[self.Material][0] * d_qt[self.Quality] * d_me[self.Method] * (100 - (100 - self.Durability) / 2) / 100

    def show_item(self):
        print('{}은 {} 공법의 {}로 만들어져 있으며, {}한 품질입니다. 현재 내구도는 {}, 블로키지는 {}'
.format(self.Name,self.Method,self.Material,self.Quality,self.Durability,self.blockage))
        print('{}x{}x{}x{}'.format(d_ma[self.Material][0],d_qt[self.Quality],d_me[self.Method],self.Durability))


test1 = item('test1','steel','legendary','futuristic',100)
test1.show_item()
test2 = item('test2','steel','awful','early',100)
test2.show_item()


test = {'1':(1,2,3)}

test['1'][2]