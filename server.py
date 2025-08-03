#!/bin/python3
#--------------------------------------------------------
# Program by Bruce Wayne
#
#
# Version   Date    Info
# 1.0       2023    Initial Version
#
#--------------------------------------------------------

from http.server import BaseHTTPRequestHandler, HTTPServer

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")  # Added charset here
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
        self.wfile.write('<body>Был получен GET-запрос.</body></html>'.encode())

def run(server_class=HTTPServer, handler_class=HttpGetHandler):  # Changed to use HttpGetHandler
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server running on port 8000...")  # Added status message
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down server...")
        httpd.server_close()

if __name__ == '__main__':
    run()
