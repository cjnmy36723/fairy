# config=utf-8
import datetime
from flask_login import UserMixin
from fairybook.common import db
from fairybook.common.data import db_query


class Book(db.Model, UserMixin):
    """
    作品实体信息
    Attributes:
        id:用户编号。
        name:名称。
        description:描述。
        image:封面图。
        hit:点击数。
        recommend:推荐数。
        updateTime:更新时间。
        created:创建时间。
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.Text, unique=True)
    image = db.Column(db.String(100), unique=True)
    hit = db.Column(db.Integer, unique=True)
    recommend = db.Column(db.Integer, unique=True)
    updateTime = db.Column(db.DateTime, unique=True)
    created = db.Column(db.DateTime, unique=True)

    __tablename__ = 'fb_book'

    def __init__(self, book_id=None, name=None, description=None, image=None):
        """
        初始化用户信息。
        Args:
            book_id (int): 作品编号
            name (string):名称
            description (string):名称
            image (string):封面图
        """
        self.id = book_id
        self.name = name
        self.description = description
        self.image = image
        self.hit = 0
        self.recommend = 0
        self.updateTime = datetime.datetime.now()
        self.created = datetime.datetime.now()


def get_book_list(page_index, page_size=10):
    """
    返回作品信息分页集合。
    Args:
        page_index: 页码。
        page_size: 页大小。

    Returns:

    """
    start_number = (page_index - 1) * page_size
    sql = 'SELECT * FROM %s ORDER BY id DESC LIMIT %s, %s' % ('fb_book', start_number, page_size)
    return db_query(sql)
