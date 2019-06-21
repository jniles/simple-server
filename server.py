#!/usr/bin/env python3
import http.server
import socketserver

# port to listen on
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

# start up our HTTP server
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
