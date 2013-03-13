'''
@author: Christoffer Ackelman
@author: Rasmus Eneman
'''

import threading
import time
import Main

class Sensors(threading.Thread):
        
    def run(self):
        global main
        while 1:
            if main.io.digitalRead(Main.leftSensorPin) == 0:
                main.engines.stop()
                #pass
            else:
                main.engines.forward()

            time.sleep(0.05)


def start(Main):
    global main
    main = Main
    
    sensors = Sensors()
    sensors.daemon = True
    sensors.start()
