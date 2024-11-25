from flask import Flask
from .routes.home import home
from .routes.auth import auth
import os

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(auth, url_prefix="/auth")

app.secret_key = os.environ.get('SECRET_KEY')