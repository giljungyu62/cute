# 서버 바닐라 만들기
import http.server

class MyServer(http.server.BaseHTTPRequestHandler):
    html = f"""
        <html>
            <head></head>
            <body>
                <h1>공추남</h1>

                <form method="GET" action="/minam">
                    <button>서버에 진실보내기</button>
                </form>

            </body>
        </html>
    """
    minam = f"""
        <html>
            <head></head>
            <body>
                <h1>새로운 페이지입니다. 공추남</h1>
            </body>
        </html>
    """
    def do_GET(self):

        if self.path == "/":
            print("슬래시 요청으로 왔어")
            print(self.path)
            print(self.command)
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(self.html.encode("utf-8"))

        if self.path == "/minam?":
            print("공욱재는 미남이다.")
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(self.html.encode("utf-8"))

server = http.server.HTTPServer(("localhost", 8000), MyServer)
print("서버 가동 : http://localhost:8000")
server.serve_forever()




