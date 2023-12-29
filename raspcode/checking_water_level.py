from gpiozero import Button 

def check_water_level():
    water_sensor = Button(16)
    if water_sensor.is_pressed == True:
            return True
    else:
            return False