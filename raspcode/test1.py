from adafruit_seesaw.seesaw import Seesaw
from time import sleep
import board
from gpiozero import LED


while True:
    sleep(5)
    pump = LED(18)

    sleep(5)
    pump.off()