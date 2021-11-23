class controller:
    def __init__(self,left_in,right_in):
        self.input_signal = (left_in,right_in)

    def is_headphone(self,y_n):
        self.headphone = bool(y_n)
        self.headphone_out = [self.headphone*self.input_signal[0]
        ,self.headphone*self.input_signal[1]]
        return self.headphone_out

    def is_powered(self,y_n):
        self.power = bool(y_n)
        return self.power,"p"

    def is_switched(self,y_n2):
        self.switch = bool(y_n2)
        return self.switch,"s"


    def is_potentiometered(self,value):
        self.potentiometered = value
        return self.potentiometered, "v"

    def out_signal_level(self):
        self.out_signal = [self.power * self.switch * self.potentiometered * self.input_signal[0]
        ,self.power * self.switch * self.potentiometered * self.input_signal[1]]
        return self.out_signal, "level"


test = controller(1,1)
test.is_headphone(False)
test.is_powered(True)
test.is_switched(False)
test.is_potentiometered(0.7)
test.out_signal_level()
test.out_signal