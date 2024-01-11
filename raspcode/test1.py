from adafruit_seesaw.seesaw import Seesaw
from time import sleep
import board
from gpiozero import LED
pump = LED(18)

while True:
    sleep(5)
    
    pump.on()
    pump.off()
    sleep(5)