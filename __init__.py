from flask import Flask
from .routes.home import home
from .routes.auth import auth
import os

app = Flask(__name__)

app.register_blueprint()

app.secret_key = os.environ.get('SECRET_KEY')