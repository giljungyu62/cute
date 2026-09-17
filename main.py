import http.server

print(http.server)
request_handler = http.server.BaseHTTPRequestHandler
http_server = http.server.HTTPServer

class Myserver(request_handler):
    def do_GET(self):
        self.send_response(200)
        self.send_header()
        self.end_headers()
        self.end_headers()
        self.wfile.write()
        

        