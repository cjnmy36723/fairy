# config=utf-8
from flask import Blueprint, render_template
from fairy.model.books import get_book_list

homeRoute = Blueprint('home', __name__, url_prefix='/', template_folder='templates')


@homeRoute.route('/')
def index():
    recommend_items = get_book_list(1, 12, 2)
    new_items = get_book_list(1, 24)

    return render_template('home/index.html', recommend_items=recommend_items, new_items=new_items)
