# 서버 만들거야

import http.server

class MyServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("길준규".encode("utf-8"))

address = ("127.0.0.1", 8080)
server = http.server.HTTPServer(address, MyServer)
server.serve_forever()

