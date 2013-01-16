'''
@author: Christoffer Ackelman
@author: Rasmus Eneman
'''

import threading
import Main

class Sensors(threading.Thread):
        
    def run(self):
        global main
        while 1:
            if main.io.digitalRead(Main.leftSensorPin):
                main.engines.stop()
            if main.io.digitalRead(Main.rightSensorPin):
                main.engines.stop()


def start(Main):
    global main
    main = Main
    
    sensors = Sensors()
    sensors.daemon = True
    sensors.start()
