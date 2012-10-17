'''
@author: Christoffer Ackelman
@author: Rasmus Eneman
'''

import os

#Constants
leftEngineCW = 2
leftEngineCCW = 3
rightEngineCW = 4
rightEngineCCW = 17
LOW = 0
HIGH = 1

INIT = "/home/pi/raspbot/trunk/src/init.sh"
GPIO = "/home/pi/raspbot/trunk/src/gpio.sh "

class Engines:
    def __init__(self):
        os.system(INIT)
    
    '''
    Go forward. 
    Make the left engine rotate counter-clockwise (forward)
    and the right engine rotate clockwise (forward).
    '''
    def forward(self):
        self.leftEngineCCW()
        self.rightEngineCW()
    
    '''
    Go backward.
    Make the left engine rotate clockwise (backward)
    and the right engine rotate counter-clockwise (backward).
    '''
    def back(self):
        self.leftEngineCW()
        self.rightEngineCCW()
    
    '''
    Turn right.
    Make the left engine rotate counter-clockwise (forward)
    and the right engine rotate counter-clockwise (backward).
    '''
    def right(self):
        self.leftEngineCCW()
        self.rightEngineCCW()
    
    '''
    Turn left.
    Make the left engine rotate clockwise (backward)
    and the right engine rotate clockwise (forward).
    '''
    def left(self):
        self.leftEngineCW()
        self.rightEngineCW()
    
    '''
    Stop.
    Set both clockwise and counter-clockwise
    rotation to LOW (off) for both engines.
    ''' 
    def stop(self):
        self.gpio(leftEngineCCW, LOW)
        self.gpio(leftEngineCW, LOW)
        self.gpio(rightEngineCCW, LOW)
        self.gpio(rightEngineCW, LOW)
    
    '''
    Makes the left engine rotate clockwise.
    Set the counter-clockwise rotation to LOW (off)
    and the clockwise rotation to HIGH (on).
    '''
    def leftEngineCW(self):
        self.gpio(leftEngineCCW, LOW)
        self.gpio(leftEngineCW, HIGH)
    
    '''
    Makes the left engine rotate counter-clockwise.
    Set the clockwise rotation to LOW (off)
    and the counter-clockwise rotation to HIGH (on).
    '''
    def leftEngineCCW(self):
        self.gpio(leftEngineCW, LOW)
        self.gpio(leftEngineCCW, HIGH)
    
    '''
    Makes the right engine rotate clockwise.
    Set the counter-clockwise rotation to LOW (off)
    and the clockwise rotation to HIGH (on).
    '''
    def rightEngineCW(self):
        self.gpio(rightEngineCCW, LOW)
        self.gpio(rightEngineCW, HIGH)
    
    '''
    Makes the right engine rotate counter-clockwise.
    Set the clockwise rotation to LOW (off)
    and the counter-clockwise rotation to HIGH (on).
    '''
    def rightEngineCCW(self):
        self.gpio(rightEngineCW, LOW)
        self.gpio(rightEngineCCW, HIGH)

    def gpio(self, pin, value):
        os.system(GPIO + str(pin) + " " + str(value))
