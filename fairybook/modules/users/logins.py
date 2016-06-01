# config=utf-8
from flask import Blueprint, request, redirect, url_for, render_template, flash, g
from flask_login import login_user, logout_user
from fairybook import login_manager
from fairybook.common import db
from fairybook.common.encrypt import md5
from fairybook.modules.users.models.users import User
from fairybook.modules.users.forms.login import LoginForm
from fairybook.modules.users.forms.register import RegisterForm
import datetime

loginRoute = Blueprint('account', __name__, url_prefix='/account', template_folder='templates')


@login_manager.user_loader
def load_user(user_id):
    """
    flask_login 库会调用该函数来加载当前用户的信息。
    Args:
        user_id:
        用户编号。
    Returns:
        用户信息。
    """
    return User.query.get(int(user_id))


@loginRoute.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('register.html', form=form)

        user = User.query.filter(User.accountNumber == form.accountNumber.data).first()

        if user:
            flash("账号已存在")
            return render_template('register.html', form=form)

        user = User()
        user.accountNumber = form.accountNumber.data
        user.password = md5(form.password.data)
        user.name = form.name.data
        user.created = datetime.datetime.now()

        db.session.add(user)
        db.session.commit()

        return render_template('login.html', form=form)

    return render_template('register.html', form=form)


@loginRoute.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('login.html', form=form)

        user = User.query.filter(User.accountNumber == form.accountNumber.data,
                                 User.password == md5(form.password.data)).first()

        if user:
            db.session.execute('UPDATE py_user SET loginTime = :loginTime WHERE id = :id',
                               {'id': user.id, 'loginTime': datetime.datetime.now()})
            db.session.commit()

            g.user = user
            login_user(user)
            return redirect("/")

    return render_template('login.html', form=form)


@loginRoute.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.login'))
