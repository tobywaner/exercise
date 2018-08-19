from app import app
from flask import render_template, request


@app.route("/")
@app.route("/index")
def index():
    return render_template("base.html")


@app.route("/results")
def show_results():
    uuid = request.args.get("suid")
    return render_template("results.html", recruit_uuid=uuid)


@app.route("/backoffice")
@app.route("/login")
@app.route("/backoffice/recruit")
@app.route("/backoffice/depart")
def login():
    return render_template("login.html")


@app.route("/backoffice/recruit/add")
def recruit_add():
    return render_template("recruit/add.html")


@app.route("/backoffice/recruit/list")
def recruit_list():
    return render_template("recruit/list.html")


@app.route("/backoffice/recruit/modify/<recruit_uuid>")
def recruit_update(recruit_uuid):
    return render_template("recruit/modify.html", recruit_uuid=recruit_uuid)


@app.route("/backoffice/recruit/detail/<recruit_uuid>")
def recruit_show(recruit_uuid):
    return render_template("recruit/detail.html", recruit_uuid=recruit_uuid)


@app.route("/backoffice/recruit/<recruit_uuid>/student/add")
def student_add(recruit_uuid):
    return render_template("student/add.html", recruit_uuid=recruit_uuid)


@app.route("/backoffice/recruit/<recruit_uuid>/student/add")
def student_add(recruit_uuid):
    return render_template("student/add.html", recruit_uuid=recruit_uuid)


@app.route("/backoffice/recruit/<recruit_uuid>/student/detail/<student_id>")
def student_show(recruit_uuid, student_id):
    return render_template("student/detail.html", recruit_uuid=recruit_uuid, student_id=student_id)


@app.route("/backoffice/depart/add")
def depart_add():
    return render_template("depart/add.html")


@app.route("/backoffice/depart/list")
def depart_list():
    return render_template("depart/list.html")


@app.route("/backoffice/depart/modify/<depart_uuid>")
def depart_update(depart_uuid):
    return render_template("depart/modify.html", depart_uuid=depart_uuid)

