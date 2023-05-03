from flask import Flask, render_template

# templates 폴더내에 html 파일이 있음을 명시
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return "Flask Test!"

@app.route("/test")
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run("0.0.0.0")