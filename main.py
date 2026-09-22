import http.server
from members_list import a




class MyServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("path 구경", self.path)



        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("공미남".encode("utf-8"))
        
        if self.path == "/minam12":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(a().encode("utf-8"))

address = ("127.0.0.1", 8080)
server = http.server.HTTPServer(address, MyServer)
print("서버 가동중 ! : http://127.0.0.1:8000")
print("서버를 종료하고 싶다면 ctrl + C")
server.serve_forever()
