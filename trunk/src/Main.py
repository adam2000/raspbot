'''
@author: Christoffer Ackelman
@author: Rasmus Eneman
'''
import time
import os
import wiringpi
import Ping
import Web
from Engines import Engines

#pwmPin = 1 #wirningPi number, rely pin 18
pwmPin = 18
leftSensorPin = 3
rightSensorPin = 17

INIT = "/home/pi/raspbot/trunk/src/init.sh"

class Main:
    def __init__(self):
        os.system(INIT)
        wiringpi.wiringPiSetupSys()
        self.io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
        #self.io.pinMode(pwmPin, self.io.PWM_OUTPUT)
        #self.io.pinMode(leftSensorPin, self.io.INPUT)
        #self.io.pinMode(rightSensorPin, self.io.INPUT)
        self.engines = Engines(self)
        Ping.start(self)
        Web.start(self)
        while 1:
            time.sleep(10)

if __name__ == '__main__':
    main = Main()
