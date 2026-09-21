# 서버 만들거야

import http.server
from members import members
from members_list import members_list

main_html = f"""
<html>
    <head></head>
    <body>
        <ul>
            {members_list(members)}
        </ul>
    </body>
</html>
"""

class MyServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(main_html.encode("utf-8"))

address = ("127.0.0.1", 8080)
server = http.server.HTTPServer(address, MyServer)
print("서버 가동중!: http://127.0.0.1:8000")
print("서버를 종료하고 싶다면 ctrl + c ")
server.serve_forever()