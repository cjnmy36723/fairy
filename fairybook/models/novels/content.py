# config=utf-8
import datetime
from flask_login import UserMixin
from fairybook.common import db
from fairybook.common.data import db_query_first


class ContentItem(db.Model, UserMixin):
    """
    小说内容实体信息
    Attributes:
        id:小说内容编号。
        novel_id:小说编号。
        title:标题。
        description:内容。
        hit:点击数。
        recommend:推荐数。
        updateTime:更新时间。
        created:创建时间。
    """
    id = db.Column(db.Integer, primary_key=True)
    novel_id = db.Column(db.Integer, unique=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text, unique=True)
    hit = db.Column(db.Integer, unique=True)
    recommend = db.Column(db.Integer, unique=True)
    updateTime = db.Column(db.DateTime, unique=True)
    created = db.Column(db.DateTime, unique=True)

    __tablename__ = 'fb_novelContent'

    def __init__(self, novel_content_id=None, novel_id=None, title=None, description=None):
        """
        初始化小说内容信息。
        Args:
            novel_content_id (int): 小说内容编号
            novel_id (int): 小说编号
            title (string):标题
            description (string):内容
        """
        self.id = novel_content_id
        self.novel_id = novel_id
        self.title = title
        self.description = description
        self.hit = 0
        self.recommend = 0
        self.updateTime = datetime.datetime.now()
        self.created = datetime.datetime.now()


def get_novel_content_by_id(content_id):
    """
    返回指定作品的小说章节内容信息。
    Args:
        content_id: 小说内容编号。
    Returns:
        小说内容信息。
    """

    return db_query_first('SELECT * FROM %s WHERE id=:content_id ORDER BY id' % ContentItem.__tablename__,
                          args={'content_id': content_id})
