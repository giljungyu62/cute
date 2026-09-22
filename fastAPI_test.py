from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# 1. 메인 페이지 (GET /)
@app.get("/", response_class=HTMLResponse)
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
@app.get("/minam", response_class=HTMLResponse)
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
