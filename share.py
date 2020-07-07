# -*- coding: utf-8 -*-
"""
python局域网共享文件夹的代码
"""
# encoding=gbk
import http.server
import socketserver

PORT = 8888
Handler = http.server.SimpleHTTPRequestHandler
# httpd=socketserver.TCPServer(("127.0.0.1",PORT),Handler)
#
httpd = socketserver.TCPServer(("", PORT), Handler)
print("http://172.31.73.103:", PORT, sep='')
httpd.serve_forever()
