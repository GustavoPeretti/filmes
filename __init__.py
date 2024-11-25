from flask import Flask
from .routes.home import home
import os

app = Flask(__name__)

app.register_blueprint(home)

app.secret_key = os.environ.get('SECRET_KEY')