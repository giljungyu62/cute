from http.server import BaseHTTPRequestHandler, HTTPServer

a = HTTPServer
b = BaseHTTPRequestHandler

print(BaseHTTPRequestHandler.error_message_format)
print(type(BaseHTTPRequestHandler.error_message_format))
print(b.error_content_type)

