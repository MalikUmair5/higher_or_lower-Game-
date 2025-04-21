def turn_on():
    global switch_on
    switch_on = True
    
def turn_off():
    global switch_on
    switch_on = False


switch_on = False;

print(switch_on)
turn_on()
print(switch_on)
turn_off()
print(switch_on)
turn_on()