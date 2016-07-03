# config=utf-8
from flask import g
from flask_login import current_user
from fairy import create_app
from fairy.controllers.home import homeRoute
from fairy.controllers.account import accountRoute
from fairy.controllers.user import userRoute
from fairy.controllers.book import bookRoute
from fairy.controllers.novel import novelRoute

DEFAULT_MODULES = [homeRoute,
                   accountRoute,
                   userRoute,
                   bookRoute,
                   novelRoute]

app = create_app('config.py')


@app.before_request
def before_request():
    """
    这里是全局的方法，在请求开始之前调用。
    其中 flask 有个全局的变量 g，它是和 session 一样的用途，可以使用它来保存当前用户的数据
    Returns:

    """
    g.user = current_user
    pass


for module in DEFAULT_MODULES:
    app.register_blueprint(module)
