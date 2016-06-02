# config=utf-8
from flask import Blueprint, render_template

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
def work_list(page_index=1):
    """
    列表
    Args:
        page_index:页码。
    """

    if page_index is not int:
        page_index = 1

    page_index = int(page_index)

    if page_index < 1:
        page_index = 1

    return render_template('book/list.html', page_index=page_index)
