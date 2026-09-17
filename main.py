import http.server

print(http.server)

request_handler = http.server.BaseHTTPRequestHandler
http_server = http.server.HTTPServer

class MyServer(request_handler):
    def do_GET(self):
        self.send_response(200) # 외우기
        self.send_header("Content-type","text/plain; charset=utf-8") # 외우기
        self.end_headers()
        self.wfile.write("나는 길준규.".encode("utf-8"))

server = http_server(("127.0.0.1", 1234), MyServer)
print("server 가동중입니다.")
server.serve_forever()