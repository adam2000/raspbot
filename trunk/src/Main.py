'''
@author: Christoffer Ackelman
'''
import Web
from Engines import Engines

class Main:
    def __init__(self):
        self.engines = Engines()
        Web.start(self)
        #engines.backward()

if __name__ == '__main__':
    main = Main()
