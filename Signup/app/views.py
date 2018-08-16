from app import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    return render_template("base.html")


@app.route('/results')
def show_results():
    uuid = request.args.get('suid')
    return render_template("results.html", recruit_uuid=uuid)


@app.route('/backoffice')
@app.route('/login')
@app.route('/backoffice/student')
@app.route('/backoffice/recruit')
@app.route('/backoffice/depart')
def login():
    return render_template("login.html")


@app.route('/backoffice/recruit/add')
def recruit_add():
    return render_template("recruit/add.html")


@app.route('/backoffice/recruit/list')
def recruit_list():
    return render_template("recruit/list.html")


@app.route('/backoffice/recruit/modify/<recruit_uuid>')
def recruit_update(recruit_uuid):
    return render_template("recruit/modify.html", recruit_uuid=recruit_uuid)


@app.route('/backoffice/recruit/detail/<recruit_uuid>')
def recruit_show(recruit_uuid):
    return render_template("recruit/detail.html", recruit_uuid=recruit_uuid)

# / backoffice / recruit / list
# / backoffice / recruit / add
# / backoffice / recruit / modify?suid = xxxx - xx - xx - xxxx
# / backoffice / recruit / detail?suid = xxxx - xx - xx - xxxx
# / backoffice / student / add?suid = xxxx - xx - xx - xxxx
# / backoffice / student / detail?suid = xxxx - xx - xx - xxxx & stid = xxxx - xx - xx - xxxx
# / backoffice / depart / add
# / backoffice / depart / list
# / backoffice / depart / modify?dtid = xxxx - xx - xx - xxxx
