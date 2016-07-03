# config=utf-8
import datetime
from flask_login import UserMixin
from fairy.common import db
from fairy.common.data import db_execute


class User(db.Model, UserMixin):
    """
    用户实体信息
    Attributes:
        id:用户编号。
        accountNumber:账号。
        password:密码。
        name:用户昵称。
        loginTime:登录时间。
        created:创建时间。
    """
    id = db.Column(db.Integer, primary_key=True)
    accountNumber = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(20), unique=True)
    loginTime = db.Column(db.DateTime, unique=True)
    created = db.Column(db.DateTime, unique=True)

    __tablename__ = 'fb_user'

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
        self.loginTime = datetime.datetime.now()
        self.created = datetime.datetime.now()

    def update_login_time(self):
        """
        更新登录时间。
        """
        db_execute('UPDATE %s SET loginTime = :loginTime WHERE id = :id' % self.__tablename__,
                   args={'id': self.id, 'loginTime': datetime.datetime.now()})

    def add(self):
        """
        创建新用户。
        """
        db.session.add(self)
        db.session.commit()
