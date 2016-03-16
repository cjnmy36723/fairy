# config=utf-8
from flask import Flask
from flask_login import LoginManager
from fairybook.common import db


"""
初始化登录管理器
"""
login_manager = LoginManager()

"""
这里的参数格式是：蓝图名称.函数名
这里是指定了当用户未登录的时候，进入需要登录才能进入的页面时，会自动跳转到的页面。
"""
login_manager.login_view = "user.login"


def create_app(config_filename=None):
    app = Flask(__name__)
    login_manager.init_app(app)

    if config_filename is not None:
        # 注册数据访问信息
        app.config.from_pyfile(config_filename)

        # 初始化数据库
        configure_database(app)

    return app


def configure_database(app):
    """初始化数据库连接。
    Args:
        app:应用对象。
    Returns:
        该函数没有返回值。
    """
    db.init_app(app)
