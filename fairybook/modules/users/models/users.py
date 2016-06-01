# config=utf-8
from flask_login import UserMixin
from fairybook.common import db


class User(db.Model, UserMixin):
    """
    用户实体信息
    Attributes:
        id:用户编号。
        accountNumber:账号。
        password:密码。
        name:用户昵称。
    """
    id = db.Column(db.Integer, primary_key=True)
    accountNumber = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(20), unique=True)
    loginTime = db.Column(db.DateTime, unique=True)
    created = db.Column(db.DateTime, unique=True)

    __tablename__ = 'py_user'

    def __init__(self, user_id=None, account_number=None, password=None, name="anonymous"):
        """
        初始化用户信息。
        Args:
            user_id (int): 用户编号
            account_number(string):账号
            password(string):密码
            name (string):昵称
        """
        self.id = user_id
        self.accountNumber = account_number
        self.password = password
        self.name = name
