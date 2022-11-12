import flask
from flask import render_template,send_file
app = flask.Flask(__name__,static_folder = 'static')
dormList = ["northeast","central","ohill","southwest","honors","sylvan"]
    
@app.route('/')
def index():
    return send_file("templates/index.html")

@app.route('/preview/<name>')
def preview(name):
    return send_file(f'templates/{name}.html')

@app.route('/dorm/<name>')
def dorm(name):
    if name not in dormList:
        return ('Not found',404)
    return render_template('dorm.html',dormName = name)
#@app.route('/quiz')
#def quiz():
#    return render_template("quiz.html")
app.run('0.0.0.0',8888)