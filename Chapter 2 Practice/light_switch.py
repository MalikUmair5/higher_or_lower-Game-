class LighSwitch():
    def __init__(self):
        self.switch_on = False
        
    def turn_on(self):
        self.switch_on = True
        
    def tun_off(self):
        self.switch_on = False



o_switch = LighSwitch()

print(o_switch.switch_on)

o_switch.turn_on()

print(o_switch.switch_on)



