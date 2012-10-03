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
    
    def forward(self):
        self.leftEngineCW()
        self.rightEngineCCW()
   
    def backward(self):
        self.leftEngineCCW()
        self.rightEngineCW()
   
    def turnRight(self):
        self.leftEngineCCW()
        self.rightEngineCCW()
   
    def turnLeft(self):
        self.leftEngineCW()
        self.rightEngineCW()
        
    def stop(self):
        wiringpi.digitalWrite(leftEngineCCW, LOW)
        wiringpi.digitalWrite(leftEngineCW, LOW)
        wiringpi.digitalWrite(rightEngineCCW, LOW)
        wiringpi.digitalWrite(rightEngineCW, LOW)
    
    def leftEngineCW(self):
        wiringpi.digitalWrite(leftEngineCCW, LOW)
        wiringpi.digitalWrite(leftEngineCW, HIGH)
    
    def leftEngineCCW(self):
        wiringpi.digitalWrite(leftEngineCW, LOW)
        wiringpi.digitalWrite(leftEngineCCW, HIGH)
    
    def rightEngineCW(self):
        wiringpi.digitalWrite(rightEngineCCW, LOW)
        wiringpi.digitalWrite(rightEngineCW, HIGH)
    
    def rightEngineCCW(self):
        wiringpi.digitalWrite(rightEngineCW, LOW)
        wiringpi.digitalWrite(rightEngineCCW, HIGH)
