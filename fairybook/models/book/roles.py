# config=utf-8
import datetime
from flask_login import UserMixin
from fairybook.common import db
from fairybook.common.data import db_query


class Role(db.Model, UserMixin):
    """
    角色实体信息
    Attributes:
        id:角色编号。
        book_id:作品编号。
        name:角色名称。
        description:描述。
        image:图片集。
        hit:点击数。
        recommend:推荐数。
        updateTime:更新时间。
        created:创建时间。
    """
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.Text, unique=True)
    image = db.Column(db.Text, unique=True)
    hit = db.Column(db.Integer, unique=True)
    recommend = db.Column(db.Integer, unique=True)
    updateTime = db.Column(db.DateTime, unique=True)
    created = db.Column(db.DateTime, unique=True)

    __tablename__ = 'fb_role'

    def __init__(self, role_id, book_id=None, name=None, description=None, image=None):
        """
        初始化角色信息。
        Args:
            role_id (int): 角色编号
            book_id (int): 作品编号
            name (string):名称
            description (string):描述
            image (string):封面图
        """
        self.id = role_id
        self.book_id = book_id
        self.name = name
        self.description = description
        self.image = image
        self.hit = 0
        self.recommend = 0
        self.updateTime = datetime.datetime.now()
        self.created = datetime.datetime.now()


def get_roles_by_book_id(book_id):
    """
    返回指定作品的角色信息集合。
    Args:
        book_id: 作品编号。
    Returns:
        角色信息集合。
    """

    return db_query('SELECT * FROM %s WHERE book_id=:book_id ORDER BY id' % Role.__tablename__,
                    args={'book_id': book_id})
