# config=utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(Form):
    accountNumber = StringField('accountNumber', validators=[DataRequired('账号不可以是空的'),
                                                             Length(-1, 200, '账号的字符数不可以超过 200 个'),
                                                             Email('账号只能是邮箱')])
    password = PasswordField('password', validators=[DataRequired('密码不可以是空的'),
                                                     Length(6, 20, '密码的字符数只能在 6 - 20 个之间')])
