# config=utf-8
import datetime
from flask_login import UserMixin
from fairybook.common import db
from fairybook.common.data import db_query


class Novel(db.Model, UserMixin):
    """
    小说实体信息
    Attributes:
        id:小说编号。
        book_id:作品编号。
        name:名称。
        description:描述。
        keyword:关键字。
        image:封面图。
        hit:点击数。
        recommend:推荐数。
        updateTime:更新时间。
        created:创建时间。
    """
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.Text, unique=True)
    keyword = db.Column(db.String(100), unique=True)
    image = db.Column(db.String(100), unique=True)
    hit = db.Column(db.Integer, unique=True)
    recommend = db.Column(db.Integer, unique=True)
    updateTime = db.Column(db.DateTime, unique=True)
    created = db.Column(db.DateTime, unique=True)

    __tablename__ = 'fb_novel'

    def __init__(self, novel_id=None, book_id=None, name=None, description=None, keyword=None, image=None):
        """
        初始化小说信息。
        Args:
            novel_id (int): 小说编号
            book_id (int): 作品编号
            name (string):名称
            description (string):描述
            keyword (string):关键字
            image (string):封面图
        """
        self.id = novel_id
        self.book_id = book_id
        self.name = name
        self.description = description
        self.keyword = keyword
        self.image = image
        self.hit = 0
        self.recommend = 0
        self.updateTime = datetime.datetime.now()
        self.created = datetime.datetime.now()


def get_novel(novel_id):
    """
    获得小说详细信息。
    Args:
        novel_id: 小说信息编号。
    Returns:
        小说的详细信息。
    """
    return Novel.query.filter(Novel.id == novel_id).first()


def get_novels(book_id):
    """
    获得指定作品的相关小说列表。
    Args:
        book_id: 作品编号

    Returns:
        指定作品的相关小说列表
    """
    return db_query('SELECT * FROM %s WHERE book_id=:book_id ORDER BY id' % Novel.__tablename__,
                    args={'book_id': book_id})
