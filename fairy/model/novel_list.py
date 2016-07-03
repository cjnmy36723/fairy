# config=utf-8
import datetime
from flask_login import UserMixin
from fairy.common import db
from fairy.common.data import db_query


class ContentList(db.Model, UserMixin):
    """
    小说目录实体信息
    Attributes:
        id:小说目录编号。
        novel_id:小说编号。
        title:标题。
        description:描述。
        hit:点击数。
        recommend:推荐数。
        updateTime:更新时间。
        created:创建时间。
    """
    id = db.Column(db.Integer, primary_key=True)
    novel_id = db.Column(db.Integer, unique=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200), unique=True)
    hit = db.Column(db.Integer, unique=True)
    recommend = db.Column(db.Integer, unique=True)
    updateTime = db.Column(db.DateTime, unique=True)
    created = db.Column(db.DateTime, unique=True)

    __tablename__ = 'fb_novelList'

    def __init__(self, novel_list_id=None, novel_id=None, title=None, description=None):
        """
        初始化小说目录信息。
        Args:
            novel_list_id (int): 小说目录编号
            novel_id (int): 小说编号
            title (string):标题
            description (string):简介
        """
        self.id = novel_list_id
        self.novel_id = novel_id
        self.title = title
        self.description = description
        self.hit = 0
        self.recommend = 0
        self.updateTime = datetime.datetime.now()
        self.created = datetime.datetime.now()


def get_novel_list_by_novel_id(novel_id):
    """
    返回指定小说的目录信息集合。
    Args:
        novel_id: 小说编号。
    Returns:
        小说目录信息集合。
    """

    return db_query('SELECT * FROM %s WHERE novel_id=:novel_id ORDER BY id' % ContentList.__tablename__,
                    args={'novel_id': novel_id})
