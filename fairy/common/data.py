# config=utf-8
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from fairy.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO


def db_query_first(sql, settings=None, echo=None, args=None):
    """
    获得单条记录。
    Args:
        sql: SQL 语句
        settings: 数据库连接字符串
        echo: 是否输出 SQL 语句
        args: SQL 参数

    Returns:

    """
    items = db_query(sql, settings, echo, args)
    if len(items) > 0:
        return items[0];


def db_query(sql, settings=None, echo=None, args=None):
    """
    获得多条记录的数组。
    Args:
        sql: SQL 语句
        settings: 数据库连接字符串
        echo: 是否输出 SQL 语句
        args: SQL 参数

    Returns:
        执行结果
    """
    if settings is None:
        settings = SQLALCHEMY_DATABASE_URI

    if echo is None:
        echo = SQLALCHEMY_ECHO

    if args is None:
        return create_engine(settings, echo=echo).connect().execute(text(sql)).fetchall()

    return create_engine(settings, echo=echo).connect().execute(text(sql), args).fetchall()


def db_execute(sql, settings=None, echo=None, args=None):
    """
    执行增删改 SQL 语句
    Args:
        sql: SQL 语句
        settings: 数据库连接字符串
        echo: 是否输出 SQL 语句
        args: SQL 参数

    Returns:
        影响行数
    """
    if settings is None:
        settings = SQLALCHEMY_DATABASE_URI

    if echo is None:
        echo = SQLALCHEMY_ECHO

    return create_engine(settings, echo=echo).connect().execute(text(sql), args).rowcount


# 测试代码
# SELECT * FROM py_user
# INSERT INTO py_user(name) VALUES('123456')
# data = db_query("SELECT * FROM fb_user")
# print(data)

# data = db_execute("INSERT INTO py_user(name) VALUES(:name)", args={'name': '123456'})
# print(data)
