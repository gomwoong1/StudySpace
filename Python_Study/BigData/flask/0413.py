from flask import Flask, render_template

app = Flask("HelloFlask")

# / URL에 대해서 home.html을 리턴해주는 API 생성
@app.route("/")
def home():
    return render_template('home.html')

# /search URL에 대해서 RESTful API 생성
@app.route("/search")
def search():
    return "Search!!!"

# 서버 구동?
app.run("0.0.0.0")