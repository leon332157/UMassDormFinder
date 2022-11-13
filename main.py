import flask
from flask import render_template, send_file
import json
from data import *
import base64

app = flask.Flask(__name__, static_folder='static')
GLOBAL_DATA = json.load(open("data.json"))


@app.route('/')
def index():
    return render_template('index.html', dormList=dormList, dormDict=dormDict)


@app.route('/preview/<name>')
def preview(name):
    return send_file(f'templates/{name}.html')


@app.route('/dorm/<name>')
def dorm(name):
    if name not in dormList:
        return ('Not found', 404)

    return render_template('dorm.html',dormName = name, dormFriendlyName=dormDict[name], dormImage=f"/static/imgs/{name}bg.jpeg", dormDis=dormDis[name], globalData=GLOBAL_DATA)


@app.route('/quiz')
def quiz():
    return send_file("templates/quiz.html")


@app.route('/photo/<email>')
def getPhoto(email):
    if email not in GLOBAL_DATA:
        return ('Not found', 404)
    photob64 = GLOBAL_DATA[email]['photo']
    if photob64 == "":
        return ('Not found', 404)
    return base64.urlsafe_b64decode(photob64), 200, {'Content-Type': GLOBAL_DATA[email]['photoType']}


@app.route('/addReview', methods=['POST'])
def addRating():
    data = flask.request.form
    photo = flask.request.files['photo']
    print(data)
    if any(str.isdigit(x) for x in data['email']):
        return flask.redirect(f"{flask.request.referrer}?submitted=false")
    email = data['email'] + '@umass.edu'
    rating = int(data['rating'])
    print(photo)
    photodata = photo.stream.read()
    b64data = base64.urlsafe_b64encode(photodata).decode('ascii')
    GLOBAL_DATA[email] = {"name": data['name'], "rating": rating, "comment": data.get(
        "comment", None), "hall": data['hall'], "area": data["area"], "photoType": photo.mimetype, "photo": b64data}
    with open('data.json', 'w') as f:
        json.dump(GLOBAL_DATA, f)
    return flask.redirect(f"{flask.request.referrer}?submitted=true")

@app.route('/favicon.ico')
def favicon():
    return flask.redirect("https://www.umass.edu/sites/default/files/favicons/favicon-32x32.png")
# @app.route('/quiz')
# def quiz():
#    return render_template("quiz.html")
app.run('0.0.0.0', 8888, debug=True)
