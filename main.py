import flask
from flask import render_template,send_file
app = flask.Flask(__name__,static_folder = 'static')
dormDict = {"northeast":"Northeast","central":"Central","ohill":"Orchard Hill","southwest":"Southwest","honors":"Honors College","sylvan":"Sylvan"}
dormList = list(dormDict.keys())

@app.route('/')
def index():
    return render_template('index.html',dormList = dormList,dormDict = dormDict)

@app.route('/preview/<name>')
def preview(name):
    return send_file(f'templates/{name}.html')

@app.route('/dorm/<name>')
def dorm(name):
    if name not in dormList:
        return ('Not found',404)
    return render_template('dorm.html',dormName = dormDict[name])

@app.route('/quiz')
def quiz():
    return send_file("templates/quiz.html")

#@app.route('/quiz')
#def quiz():
#    return render_template("quiz.html")
app.run('0.0.0.0',8888)