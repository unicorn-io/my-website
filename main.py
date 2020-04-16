from flask import Blueprint
from flask import render_template
from flask import redirect

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

@main.route("/projects")
def interest_page():
    return render_template("portfolio.html")