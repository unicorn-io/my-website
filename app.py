# app.py
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contacts')
def contacts_page():
    return render_template("contacts.html")

@app.route('/resume')
def resume_page():
    return render_template("resume.html")

@app.route("/projects")
def interest_page():
    return render_template("portfolio.html")

if __name__=="__main__":
    app.run()