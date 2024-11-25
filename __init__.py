from flask import Flask
from .routes.home import home
from .routes.auth import auth
from .routes.api import api
import os

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(api, url_prefix='/api')

app.secret_key = os.environ.get('SECRET_KEY')