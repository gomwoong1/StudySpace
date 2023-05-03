from flask import Flask

app = Flask("TestFlask")

@app.route("/")
def home():
    return "Flask Test!"

app.run("0.0.0.0")