from gpiozero import Button 

water_sensor = Button(16)

if water_sensor.is_pressed == True:
        print("water")
else:
        print("no water")