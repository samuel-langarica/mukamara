# server.py
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class WebAppHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='build/web', **kwargs)

def run(server_class=HTTPServer, handler_class=WebAppHandler):
    port = int(os.environ.get('PORT', 8080))
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()