from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template("base.html")

# /
# index
# nothing, only
# show
# a
# blank(no
# need
# login)
#
# / recruit?suid = xxxx - xx - xx - xxxx
# a
# sign
# up
# page(no
# need
# login)
#
# / results?suid = xxxx - xx - xx - xxxx
# sign
# up
# result(maybe
# need
# cookie
# support)(no need login)
#
# / backoffice
# / login
# / backoffice / student
# / backoffice / recruit
# / backoffice / depart
# login
# page
#
# / backoffice / recruit / list
# / backoffice / recruit / add
# / backoffice / recruit / modify?suid = xxxx - xx - xx - xxxx
# / backoffice / recruit / detail?suid = xxxx - xx - xx - xxxx
# / backoffice / student / add?suid = xxxx - xx - xx - xxxx
# / backoffice / student / detail?suid = xxxx - xx - xx - xxxx & stid = xxxx - xx - xx - xxxx
# / backoffice / depart / add
# / backoffice / depart / list
# / backoffice / depart / modify?dtid = xxxx - xx - xx - xxxx