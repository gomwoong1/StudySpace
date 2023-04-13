from flask import Flask

app = Flask("HelloFlask")

# / URL에 대해서 RESTful API 생성
@app.route("/")
def home():
    return "Hello Flask!!!"

# /search URL에 대해서 RESTful API 생성
@app.route("/search")
def search():
    return "Search!!!"

# 서버 구동?
app.run("0.0.0.0")