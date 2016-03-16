# config=utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    accountNumber = StringField('accountNumber', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
