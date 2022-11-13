import flask
from flask import render_template,send_file
app = flask.Flask(__name__,static_folder = 'static')
dormDict = {"northeast":"Northeast","central":"Central","ohill":"Orchard Hill","southwest":"Southwest","honors":"Honors College","sylvan":"Sylvan"}
dormList = list(dormDict.keys())
dormDis = {"northeast":"""First Year Halls: located in Crabtree, Dwight, Hamlin, Leach, Mary Lyon and Knowlton
Right next to Worcester Dining Commons
Close proximity to Campus Center, College of Engineering, School of Education, School of Public Health & Health Sciences, Totman Gym
Volleyball court in the quad""",
"central":"""First-Year Halls: located in Butterfield, Gorman Hall, Van Meter Hall,Wheeler Hall
Defined Residential Communities: Spectrum Community for Gay, Lesbian, Bisexual, Transgender students, and allies.
Near Franklin Dining Commons
Close proximity to the Studio Arts building, Fine Arts Center, University Health Services, Isenberg School of Management""",
"ohill":"""First-Year Halls: located in: Dickinson and Webster Halls
Sweets n’ More in Field Hall
7-minute walk to Franklin or Worcester Dining Commons
Overlooking campus, amid rolling hills and apple trees
Daily exercise""",
"southwest":"""First-Year Halls: located in Melville, Thoreau, Pierpont , Moore, James, Emerson, Kennedy, and Cance Halls
Defined Residential Communities": ​Harambee: African Heritage Student Program in Coolidge Hall, El Barrio Community in Washington Hall 
Near Berkshire and Hampshire Dining Commons
Close proximity to Hampden Student Center, Southwest Area Government offices, Boyden Gym, Isenberg School of Management""",
"honors":"""First Year Halls:  Oak and Sycamore
Honors Advising Center
Roots Cafe
Faculty in Residence
Close proximity to Library, Campus Recreation Center, Student Union, Campus Center, Mullins Center, and Intramural Fields""",
"sylvan":"""RFYE/Transfer Community in McNamara Hall 
Fire pits available for student use
Basketball court
Snack bar in McNamara
Wooded trails"""}
#print(dormDis[])

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
    return render_template('dorm.html',dormName = dormDict[name],dormImage = f"/static/imgs/{name}bg.jpeg",dormDis = dormDis[name])

@app.route('/quiz')
def quiz():
    return send_file("templates/quiz.html")

#@app.route('/quiz')
#def quiz():
#    return render_template("quiz.html")
app.run('0.0.0.0',8888)