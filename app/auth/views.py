from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from ..models import User
from . forms import LoginForm
from . import auth
from flask_login import logout_user, login_required



@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = user.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
            flash('Invaid username or password')
        return render_template('auth/login.html')



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out.')
    return redirect(url_for('main.index'))
