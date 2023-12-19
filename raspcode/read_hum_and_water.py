from adafruit_seesaw.seesaw import Seesaw
from time import sleep
import board
from gpiozero import LED

def check():
    pump = LED(18)

    i2c_bus = board.I2C()

    ss = Seesaw(i2c_bus, addr=0x36)

    while True:

        hum = ss.moisture_read()


        temp = ss.get_temp()
        if int(hum) < 600:
            pump.on()
            pump.off()
            sleep(15)
        print("temp: " + str(temp) + "  moisture: " + str(hum))
        sleep(1)