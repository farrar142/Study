import time

class counter:
    counter_list = []
    coin_counter = []
    def __init__(self,*what): ## 카운터 생성
        for i in what:
            self.counter_list.append(i)

    def what_you_have(self): # 카운터 확인
        print(self.counter_list,"목표값")
        print(self.coin_counter,"시작값")

    def counter_init(self): # 카운터 올릴놈 생성
        for i in self.counter_list:
            self.coin_counter.append(0)

    def counter_start(self): # 카운터 올릴놈을 카운터 까지
            while self.counter_list != self.coin_counter:              
                for i in range(0,len(self.coin_counter)):
                    if self.coin_counter[i] < self.counter_list[i]:
                        self.coin_counter[i] = self.coin_counter[i] + 1
                print(self.coin_counter)            
                time.sleep(0.1)


a = counter(4,9,36,2,3,5,6,7,8)

a. counter_init()

a.what_you_have()

a.counter_start()