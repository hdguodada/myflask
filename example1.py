from flask import Flask, url_for
from flask import render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



app = Flask(__name__)
app.config['SECRET_KEY'] = 'NIDAYE'
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


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


class NameForm(Form):
    name = StringField('what is your name ?', validators=[DataRequired()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    app.run()


