from flask import Flask, render_template, request, jsonify
import model
from AI.report.rep_4 import peopleRegression

# templates 폴더내에 html 파일이 있음을 명시
app = Flask(__name__, template_folder='templates')


@app.route("/lr")
def lr():
    return render_template('lr.html')

# /r/value url로 POST API 생성
@app.route("/lr/value", methods=['POST'])
def lr_val():
    # HTTP BODY의 데이터를 request객체의 get_json() 함수로 받아옴
    # JSON 형식으로 받아오고 이를 data 변수에 저장
    data = request.get_json()
    
    # 모델 서빙을 위해 만든 클래스의 객체 생성
    plr = peopleRegression()
    # 객체의 
    res = plr.predict(int(data))

    normal = []
    danger = []
    high_danger = []

    for key, value in res.items():
        if value > 0.5:
            normal.append("{}({})".format(key, value))
        elif value > 0.2:
            danger.append("{}({})".format(key, value))
        else:
            high_danger.append("{}({})".format(key, value))

    if len(normal) == 0:
        normal = ['없음']
    
    if len(danger) == 0:
        danger = ['없음']

    if len(high_danger) == 0:
        high_danger = ['없음']

    return jsonify({"normal": normal, "danger":danger, "high_danger":high_danger})

# 
@app.route("/")
def home():
    return "Flask Test!"

@app.route("/test")
def test():
    return render_template('test.html')

# form 방식 Test
# request 라이브러리 import 필요, route 함수에 method 기입할 것
@app.route('/formData', methods=['POST'])
def formData():
    data = request.form['text']
    return "서버로부터 돌아온 답변: " + data + " 입니다!"

# json 방식 Test
@app.route('/jsonData', methods=['POST'])
def jsonData():
    data = request.get_json()
    print("data JSON:", data)

    return jsonify({"PData": "서버에서 보낸 데이터: " + data})

# Query String Test
# http://localhost:5000/QueryData?data=
@app.route('/QueryData')
def queryData():
    data = request.args.get('data')
    return "서버로부터 돌아온 답변: " + data + " 입니다!"

# POST 방식으로 시간을 전달받으면 결과값 연산 후 돌려줌
@app.route('/predictTest', methods=['POST'])
def predictTest():
    hour = float(request.get_json())
    test = model.LinearRegression()
    result = str(test.predict(hour))

    return jsonify({"predict": "예상 점수는 " + result + "점 입니다."})

if __name__ == '__main__':
    app.run("0.0.0.0")