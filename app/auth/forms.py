from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email


class LoginForm(Form):
    '登录表单'
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in ')
    sumbit = SubmitField('Log In')
