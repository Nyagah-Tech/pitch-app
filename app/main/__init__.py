from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,error

def create_app(config_name):
    app =Flask