from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask_mail import Message

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/contacts')
def contacts_page():
    return render_template("contacts.html")

@main.route('/resume')
def resume_page():
    return render_template("resume.html")

@main.route("/portfolio")
def interest_page():
    return render_template("portfolio.html")

@main.route("/submitmsg", methods = ['POST', 'GET'])
def msg():
        result = request.form
        print(result)
        return redirect("/contacts")