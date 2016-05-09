# config=utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class RegisterForm(Form):
    accountNumber = StringField('accountNumber', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
