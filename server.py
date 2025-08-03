#!/bin/python3
#--------------------------------------------------------
# Program by Bruce Wayne
#
#
# Version   Date    Info
# 1.0       2023    Initial Version
# 1.1       2024    Few fixes
#--------------------------------------------------------

from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPHandler(BaseHTTPRequestHandler):
    """Handler for GET requests with UTF-8 support"""
    
    def send_html_response(self, content):
        """Helper method to send HTML responses"""
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))
    
    def do_GET(self):
        """Handle GET requests"""
        html_content = """
        <html>
            <head>
                <meta charset="utf-8">
                <title>Простой HTTP-сервер.</title>
            </head>
            <body>Был получен GET-запрос.</body>
        </html>
        """
        self.send_html_response(html_content)

def start_server(port=8000):
    """Start the HTTP server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPHandler)
    
    print(f"Server running on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()

if __name__ == '__main__':
    start_server()

