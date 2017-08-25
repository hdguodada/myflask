from flask import Flask, url_for, flash
from flask import render_template, session, redirect
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = 'NIDAYE'
manager = Manager(app)
bootstrap = Bootstrap(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:passwd@localhost/myflask'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


# 动态路由 + 请求上下文 + 重定向
@app.route('/user/<name>')
def user(name):
    print(url_for('user', name=name, _external=True))
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


class NameForm(FlaskForm):
    name = StringField('what is your name ?', validators=[DataRequired()])
    submit = SubmitField('Submit')


# 定义模型
class Role(db.Model):
    __tablename__ = 'roles'  # 定义数据库中使用到表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r' % self.username



    

if __name__ == '__main__':
    manager.run()


