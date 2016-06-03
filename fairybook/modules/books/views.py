# config=utf-8
from flask import Blueprint, render_template
from fairybook.modules.books.models.books import get_book_list, get_book
from fairybook.modules.books.models.roles import get_roles_by_book_id

# 这里的 templates 的路径是该配置所在目录下的 templates 目录。
bookRoute = Blueprint('book', __name__, url_prefix='/book', template_folder='templates')


@bookRoute.route('/')
@bookRoute.route('/index/')
def index():
    """
    首页
    """

    return render_template('book/index.html')


@bookRoute.route('/list/')
@bookRoute.route('/list/<page_index>/')
def book_list(page_index="1"):
    """
    列表
    Args:
        page_index:页码。
    """

    if not page_index.isdigit():
        page_index = 1

    page_index = int(page_index)

    if page_index < 1:
        page_index = 1

    items = get_book_list(page_index, 10)

    return render_template('book/list.html', page_index=page_index, items=items)


@bookRoute.route('/detail/<book_id>/')
def book_detail(book_id=None):
    """
    作品详情。
    Args:
        book_id: 作品编号。
    Returns:
        视图
    """
    book = None
    roles = None

    # 判断 book_id 是否是数字
    if book_id.isdigit():
        book = get_book(book_id)

    if book:
        roles = get_roles_by_book_id(book_id)

    return render_template('book/detail.html', book=book, roles=roles)
