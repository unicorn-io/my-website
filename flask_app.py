# app.py
from flask import Flask           # import flask
from flask import render_template
from flask_mail import Mail, Message
from flask import redirect
from flask import request

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'visheshsciensism@gmail.com'
app.config['MAIL_PASSWORD'] = 'ohyeah!!!!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contacts')
def contacts_page():
    return render_template("contacts.html")

@app.route('/resume')
def resume_page():
    return render_template("resume.html")

@app.route("/portfolio")
def interest_page():
    return render_template("portfolio.html")

@app.route('/submitmsg', methods = ['POST', 'GET'])
def msg():
    result = dict(request.form)
    msg = Message(result['name'], sender = 'visheshsciensism@gmail.com', recipients=['tayalvishesh83@gmail.com'])
    msg.body = result['message']
    mail.send(msg)
    return redirect('/contacts')

if __name__=="__main__":
    app.run()
