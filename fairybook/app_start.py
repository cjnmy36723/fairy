# config=utf-8
from flask import g
from flask_login import current_user
from fairybook import create_app
from fairybook.modules.home.views import homeRoute
from fairybook.modules.users.logins import loginRoute
from fairybook.modules.users.views import userRoute
from fairybook.modules.books.views import bookRoute
from fairybook.modules.novels.views import novelRoute

DEFAULT_MODULES = [homeRoute,
                   loginRoute,
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
