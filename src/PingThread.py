import time
import threading
import Main

# import gpio module
import RPi.GPIO as GPIO

class PingThread(threading.Thread):
    def run(self):
        global main
        delta = 0.0001
        timeSensor1 = 0 # The time that sensor 1 has given high output signal.
        timeSensor2 = 0 # The time that sensor 2 has given high output signal.
        
        while 1:
            if GPIO.input(17) == 1:
                timeSensor1 += delta
            else
                timeSensor1 = 0
            
            if GPIO.input(3) == 1:
                timeSensor2 += delta
            else
                timeSensor2 = 0
            
            time.sleep(delta)

def start(Main):
    global main
    main = Main

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3, GPIO.IN)
    GPIO.setup(17, GPIO.IN)

    ping = PingThread()
    ping.deamon = True
    ping.start()
