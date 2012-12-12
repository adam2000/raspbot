'''
@author: Christoffer Ackelman
'''
import time
import os
import wiringpi
import Sensors
import Web
from Engines import Engines

pwmPin = 1 #wirningPi number, rely pin 18

INIT = "/home/pi/raspbot/trunk/src/init.sh"

class Main:
    def __init__(self):
        os.system(INIT)
        self.io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
        self.io.pinMode(pwmPin, self.io.PWM_OUTPUT)
        self.engines = Engines(self)
        Sensors.start(self)
        Web.start(self)
        while 1:
            time.sleep(10)

if __name__ == '__main__':
    main = Main()
