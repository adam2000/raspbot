#!/usr/bin/python
# speed of sound 1126 feet per second
#13512 inches per second 
# import time module
import time
import threading
import Main

# import gpio module
import RPi.GPIO as GPIO

class Ping(threading.Thread):
    def run(self):
        global main
        while 1:
            start = 0
            end = 0
            delta = 0

            while GPIO.input(3) == 1:
                time.sleep(0.0001)
            start = time.time()
            while GPIO.input(3) == 1:
                pass
            end = time.time()
            delta = end - start
            if delta < 0.02:
                main.engines.left()
            else:
                main.engines.forward()

def start(Main):
    global main
    main = Main

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3, GPIO.IN)

    ping = Ping()
    ping.deamon = True
    ping.start()
