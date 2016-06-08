# config=utf-8
from fairybook.models.novels.content import get_novel_content_by_id
from fairybook.models.novels.list import get_novel_list_by_novel_id
from flask import Blueprint, render_template

from fairybook.models.novels.novel import get_novel

# 这里的 templates 的路径是该配置所在目录下的 templates 目录。
novelRoute = Blueprint('novel', __name__, url_prefix='/novel', template_folder='templates')


@novelRoute.route('/index/<novel_id>/')
def index(novel_id=None):
    """
    作品详情。
    Args:
        novel_id: 小说编号。
    Returns:
        视图
    """

    novel = None
    items = None

    if novel_id.isdigit():
        novel = get_novel(novel_id)
        items = get_novel_list_by_novel_id(novel_id)

    return render_template('novel/index.html', novel=novel, items=items)


@novelRoute.route('/read/<content_id>/')
def detail(content_id=None):
    """
    小说内容。
    Args:
        content_id: 小说内容编号。
    Returns:
        视图
    """
    content = None

    # 判断 content_id 是否是数字
    if content_id.isdigit():
        content = get_novel_content_by_id(content_id)

    return render_template('novel/detail.html', content=content)
