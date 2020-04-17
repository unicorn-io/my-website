from flask import Flask
from flask_mail import Mail

def create_app():
    mail = Mail()
    app = Flask(__name__)
    mail.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app