# 서버 만들거야

import http.server

class MyServer():
    insa = "hello"

    def hello():
        return "안녕?"


test = MyServer()
test.hello()
print(test.insa)
