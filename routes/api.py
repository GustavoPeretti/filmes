from flask import Blueprint
from .lista import lista
from .filme import filme

api = Blueprint('api', __name__)

api.register_blueprint(lista, url_prefix='/lista')
api.register_blueprint(filme, url_prefix='/filme')
