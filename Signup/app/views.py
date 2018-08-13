from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template("base.html")


@app.route('/results')
def show_results():
    return render_template("results.html")


@app.route('/backoffice')
@app.route('/login')
@app.route('/backoffice/student')
@app.route('/backoffice/recruit')
@app.route('/backoffice/depart')
def login():
    return render_template("login.html")


@app.route('/backoffice/recruit/list')
def recruit_add():
    return render_template("recruit/add.html")

# / backoffice / recruit / list
# / backoffice / recruit / add
# / backoffice / recruit / modify?suid = xxxx - xx - xx - xxxx
# / backoffice / recruit / detail?suid = xxxx - xx - xx - xxxx
# / backoffice / student / add?suid = xxxx - xx - xx - xxxx
# / backoffice / student / detail?suid = xxxx - xx - xx - xxxx & stid = xxxx - xx - xx - xxxx
# / backoffice / depart / add
# / backoffice / depart / list
# / backoffice / depart / modify?dtid = xxxx - xx - xx - xxxx
