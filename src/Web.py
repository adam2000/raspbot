'''
@author: Rasmus Eneman
'''

import threading
import urllib2
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class WebServer(BaseHTTPRequestHandler):

    def do_GET(self):
        global main
        
        try:
            print self.path
            self.path = urllib2.unquote(self.path)
            print self.path
            if self.path == "/":
                f = open(curdir + sep + "web" + sep + "index.html")

                self.send_response(200)
                #self.send_header('Content-type',    'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return

            elif self.path.startswith("/engines/"):
                if self.path == "/engines/forward":
                    main.engines.forward()
                elif self.path == "/engines/back":
                    main.engines.back()
                elif self.path == "/engines/left":
                    main.engines.left()
                elif self.path == "/engines/right":
                    main.engines.right()
                elif self.path == "/engines/stop":
                    main.engines.stop()
                elif self.path.startswith("/engines/speed="):
                    speed = int(self.path.split("=")[1])
                    print(speed)
                    main.engines.speed(speed)

                self.send_response(200)
                #self.send_header("Location", "/")
                self.end_headers()
                self.wfile.write(self.path)

            else:
                f = open(curdir + sep + "web" + sep + self.path)
                self.send_response(200)
                #self.send_header('Content-type',    'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                return

            return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

class Web(threading.Thread):

    def run(self):
        server = None
        try:
            server = HTTPServer(('', 80), WebServer)
            print 'started httpserver...'
            server.serve_forever()
        except KeyboardInterrupt:
            print '^C received, shutting down server'
            if server is not None:
                server.socket.close()

def start(Main):
    global main
    main = Main
    
    web = Web()
    web.daemon = True
    web.start()
