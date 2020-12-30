#!/usr/bin/env python

import http.server
import socketserver

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")


if __name__ == '__main__':
	server_address = ('127.0.0.1', 8000)
#	handler = MyHTTPRequestHandler()
	with socketserver.TCPServer(server_address, MyHTTPRequestHandler) as httpd:
		httpd.serve_forever()

