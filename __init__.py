from flask import Flask
import os

app = Flask(__name__)

app.register_blueprint()

app.secret_key = os.environ.get('SECRET_KEY')