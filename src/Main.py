'''
@author: Christoffer Ackelman
'''
import Web
from Engines import Engines

class Main:
    def __init__(self):
        global engines
        engines = Engines()
        Web.start()
        #engines.backward()

if __name__ == '__main__':
    main = Main()
