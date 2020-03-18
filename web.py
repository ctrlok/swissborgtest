#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json

PORT_NUMBER = 8080


class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # Send the html message
        if self.path == "/will":
            self.wfile.write(json.dumps("Hello World"))
        elif self.path == "/ready":
            self.wfile.write(json.dumps("It works!"))
        return


try:
    # Create a web server and define the handler
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ', PORT_NUMBER

    # Wait for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    server.socket.close()
