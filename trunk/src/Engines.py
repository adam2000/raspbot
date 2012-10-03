'''
@author: Christoffer Ackelman
@author: Rasmus Eneman
'''

import wiringpi

#Constants
leftEngineCW = 2
leftEngineCCW = 3
rightEngineCW = 4
rightEngineCCW = 17
OUTPUT = 1
LOW = 0
HIGH = 1

class Engines:
    def __init__(self):
        wiringpi.wiringPiSetup()
        wiringpi.pinMode(leftEngineCW, OUTPUT)
        wiringpi.pinMode(leftEngineCCW, OUTPUT)
        wiringpi.pinMode(rightEngineCW, OUTPUT)
        wiringpi.pinMode(rightEngineCCW, OUTPUT)
    
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
    def backward(self):
        self.leftEngineCW()
        self.rightEngineCCW()
    
    '''
    Turn right.
    Make the left engine rotate counter-clockwise (forward)
    and the right engine rotate counter-clockwise (backward).
    '''
    def turnRight(self):
        self.leftEngineCCW()
        self.rightEngineCCW()
    
    '''
    Turn left.
    Make the left engine rotate clockwise (backward)
    and the right engine rotate clockwise (forward).
    '''
    def turnLeft(self):
        self.leftEngineCW()
        self.rightEngineCW()
    
    '''
    Stop.
    Set both clockwise and counter-clockwise
    rotation to LOW (off) for both engines.
    ''' 
    def stop(self):
        wiringpi.digitalWrite(leftEngineCCW, LOW)
        wiringpi.digitalWrite(leftEngineCW, LOW)
        wiringpi.digitalWrite(rightEngineCCW, LOW)
        wiringpi.digitalWrite(rightEngineCW, LOW)
    
    '''
    Makes the left engine rotate clockwise.
    Set the counter-clockwise rotation to LOW (off)
    and the clockwise rotation to HIGH (on).
    '''
    def leftEngineCW(self):
        wiringpi.digitalWrite(leftEngineCCW, LOW)
        wiringpi.digitalWrite(leftEngineCW, HIGH)
    
    '''
    Makes the left engine rotate counter-clockwise.
    Set the clockwise rotation to LOW (off)
    and the counter-clockwise rotation to HIGH (on).
    '''
    def leftEngineCCW(self):
        wiringpi.digitalWrite(leftEngineCW, LOW)
        wiringpi.digitalWrite(leftEngineCCW, HIGH)
    
    '''
    Makes the right engine rotate clockwise.
    Set the counter-clockwise rotation to LOW (off)
    and the clockwise rotation to HIGH (on).
    '''
    def rightEngineCW(self):
        wiringpi.digitalWrite(rightEngineCCW, LOW)
        wiringpi.digitalWrite(rightEngineCW, HIGH)
    
    '''
    Makes the right engine rotate counter-clockwise.
    Set the clockwise rotation to LOW (off)
    and the counter-clockwise rotation to HIGH (on).
    '''
    def rightEngineCCW(self):
        wiringpi.digitalWrite(rightEngineCW, LOW)
        wiringpi.digitalWrite(rightEngineCCW, HIGH)
