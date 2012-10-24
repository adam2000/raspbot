import threading
import urllib2
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class WebServer(BaseHTTPRequestHandler):

    def do_GET(self):
        global engines
        
        try:
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

            elif self.path == "/forward":
                engines.forward()
                self.send_response(200)
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
        try:
            server = HTTPServer(('', 8080), WebServer)
            print 'started httpserver...'
            server.serve_forever()
        except KeyboardInterrupt:
            print '^C received, shutting down server'
            server.socket.close()

def start():
    web = Web()
    web.start()