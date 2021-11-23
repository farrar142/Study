class human:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(self.name)

hamsik = human("ham")
a = hamsik.show()

def s(something):
    something.show()

s(hamsik)