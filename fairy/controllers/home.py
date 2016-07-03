# config=utf-8
from flask import Blueprint, render_template

homeRoute = Blueprint('home', __name__, url_prefix='/', template_folder='templates')


@homeRoute.route('/')
def index():
    return render_template('home/index.html')
