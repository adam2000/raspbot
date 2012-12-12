'''
@author: Christoffer Ackelman
@author: Rasmus Eneman
'''

import os

#Constants
leftEngineCW = 2
#leftEngineCCW = 3
rightEngineCW = 4
#rightEngineCCW = 17
pwmPin = 1 #wirningPi number, rely pin 18
LOW = 0
HIGH = 1

GPIO = "/home/pi/raspbot/trunk/src/gpio.sh "

class Engines:
    lastSpeed = 1024 #Start at full speed

    def __init__(self, main):
        self.main = main
        self.off()

    '''
    Turns on the engines at the last used speed
    '''
    def on(self):
        self.main.io.pwmWrite(pwmPin, self.lastSpeed)

    '''
    Turns on the engines at the specified speed
    '''
    def speed(self, speed):
        self.lastSpeed = speed
        self.main.io.pwmWrite(pwmPin, speed)

    '''
    Turns off the engines
    '''
    def off(self):
        self.main.io.pwmWrite(pwmPin, LOW)

    '''
    Go forward.
    Make the left engine rotate counter-clockwise (forward)
    and the right engine rotate clockwise (forward).
    '''
    def forward(self):
        self.leftEngineCCW()
        self.rightEngineCW()
        self.on()

    '''
    Go backward.
    Make the left engine rotate clockwise (backward)
    and the right engine rotate counter-clockwise (backward).
    '''
    def back(self):
        self.leftEngineCW()
        self.rightEngineCCW()
        self.on()

    '''
    Turn right.
    Make the left engine rotate counter-clockwise (forward)
    and the right engine rotate counter-clockwise (backward).
    '''
    def right(self):
        self.leftEngineCCW()
        self.rightEngineCCW()
        self.on()

    '''
    Turn left.
    Make the left engine rotate clockwise (backward)
    and the right engine rotate clockwise (forward).
    '''
    def left(self):
        self.leftEngineCW()
        self.rightEngineCW()
        self.on()

    '''
    Stop.
    Set both clockwise and counter-clockwise
    rotation to LOW (off) for both engines.
    '''
    def stop(self):
        self.off()
        self.gpio(leftEngineCW, LOW)
        self.gpio(rightEngineCW, LOW)

    '''
    Makes the left engine rotate clockwise.
    Set the counter-clockwise rotation to LOW (off)
    and the clockwise rotation to HIGH (on).
    '''
    def leftEngineCW(self):
        self.gpio(leftEngineCW, HIGH)

    '''
    Makes the left engine rotate counter-clockwise.
    Set the clockwise rotation to LOW (off)
    and the counter-clockwise rotation to HIGH (on).
    '''
    def leftEngineCCW(self):
        self.gpio(leftEngineCW, LOW)

    '''
    Makes the right engine rotate clockwise.
    Set the counter-clockwise rotation to LOW (off)
    and the clockwise rotation to HIGH (on).
    '''
    def rightEngineCW(self):
        self.gpio(rightEngineCW, LOW)

    '''
    Makes the right engine rotate counter-clockwise.
    Set the clockwise rotation to LOW (off)
    and the counter-clockwise rotation to HIGH (on).
    '''
    def rightEngineCCW(self):
        self.gpio(rightEngineCW, HIGH)

    def gpio(self, pin, value):
        os.system(GPIO + str(pin) + " " + str(value))
