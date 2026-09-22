from flask import Flask

app = Flask(__name__)

# 1. 메인 페이지 (GET /)
@app.route("/")
def home():
    print("슬래시 요청으로 왔어")
    return """
        <html>
            <head><meta charset="utf-8"></head>
            <body>
                <h1>공추남</h1>
                <form method="GET" action="/minam">
                    <button>서버에 진실보내기</button>
                </form>
            </body>
        </html>
    """

# 2. 미남 페이지 (GET /minam)
@app.route("/minam")
def minam():
    print("공욱재는 미남이다.")
    return """
        <html>
            <head><meta charset="utf-8"></head>
            <body>
                <h1>새로운 페이지입니다. 공추남</h1>
            </body>
        </html>
    """

if __name__ == "__main__":
    print("서버 가동 : http://localhost:8000")
    app.run(host="localhost", port=8000, debug=True)
