from flask import Flask, url_for
from flask import request
from flask import render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    name = None
    form = NameForm()


# 动态路由 + 请求上下文
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


class NameForm(Form)


if __name__ == '__main__':
    manager.run()


