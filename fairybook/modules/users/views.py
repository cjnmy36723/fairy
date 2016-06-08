# config=utf-8
from flask import Blueprint, render_template
from flask_login import current_user, login_required

from fairybook.models.users.users import User

# 这里的 templates 的路径是该配置所在目录下的 templates 目录。
userRoute = Blueprint('user', __name__, url_prefix='/user', template_folder='templates')


@userRoute.route('/')
@userRoute.route('/<id>/')
def index(user_id=None):
    """
    搜索并显示指定编号的用户的信息
    查询出用户编号是 id 的用户的信息集合，并从中取出第一条数据。
    Args:
        user_id:用户编号
    """
    if user_id is None:
        user = current_user
    else:
        user = User.query.filter_by(id=id).first()

    return render_template('user/index.html', user=user)


@userRoute.route('/test/')
@login_required
def test():
    """
    login_required 表示已登录了才能访问，必须放在 route 的下面才有效。
    """
    return "123456"
