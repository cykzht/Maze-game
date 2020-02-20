#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import http.server
import socketserver
Handler=http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",80),Handler) as httpd:
    print("服务器运行在80端口")
    httpd.serve_forever()
