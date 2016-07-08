# config=utf-8
from flask import Blueprint, render_template
from fairy.model.books import get_book_list

homeRoute = Blueprint('home', __name__, url_prefix='/', template_folder='templates')


@homeRoute.route('/')
def index():
    items = get_book_list(1, 10)

    return render_template('home/index.html', items=items)
