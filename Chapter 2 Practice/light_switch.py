class LighSwitch():
    def __init__(self, name):
        self.switch_on = False
        self.name = name
        
    def turn_on(self):
        self.switch_on = True
        
    def turn_off(self):
        self.switch_on = False
        
    def show(self):
        print(f'{self.name} switch is {self.switch_on}')



o_switch_1 = LighSwitch("Switch 1")
o_switch_2 = LighSwitch("Switch 2")

o_switch_1.show()
o_switch_2.show()

o_switch_1.turn_on()
o_switch_2.turn_off()

o_switch_2.show()
o_switch_1.show()



