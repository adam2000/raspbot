'''
@author: Christoffer Ackelman
'''

import threading

class Sensors(threading.Thread):
        
    def run(self):
        pass


def start(Main):
    global main
    main = Main
    
    sensors = Sensors()
    sensors.daemon = True
    sensors.start()
