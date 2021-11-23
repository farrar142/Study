class Uniform:    
    def __init__(self):
        self.uniform = 1
        self.possible = 0
    def count(self):
        if self.uniform >= 1:
            return 1
        else:
            return 0
def solution(n, lost, reserve):
    student = []
    for i in range(0,n):
        i = Uniform()
        student.append(i)
    for i in reserve:
        student[i-1].uniform += 1
        student[i-1].possible = 1
    for i in lost:
        student[i-1].uniform -= 1
        student[i-1].possible = 0
        
    for index in range(0,len(student)):
        if student[index].uniform == 0:
            for k in [-1,1]:
                try:
                    if student[index+k].possible == 1 and student[index].uniform == 0 and(index+k >= 0):
                        student[index+k].uniform -= 1
                        student[index+k].possible = 0
                        student[index].uniform = 1
                except:
                    pass
    return sum([i.count() for i in student])
    



n = 3
lost = [2]
reserve = [1]

solution(n,lost,reserve)