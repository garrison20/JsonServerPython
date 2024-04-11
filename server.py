from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
import datetime

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
    # GET - send back time as json
    def do_GET(self):
        self._set_headers()

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        
        self.wfile.write(json.dumps({'currentDateTime': now}).encode()) # call encode() to convert string to bytes
        
    # POST
    def do_POST(self):
        print('Do nothing on POST')
        
def run(server_class=HTTPServer, handler_class=Server, port=8008):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print('Starting httpd on port %d...' % port)
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()