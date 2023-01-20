from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = EmailField('email',
                       validators=[
                           DataRequired(),
                           Length(1, 64),
                           Email()
                       ])

    password = PasswordField('password',
                             validators=[
                                 DataRequired(),
                             ])

    remember_me = BooleanField('Keep me logged in.')

    submit = SubmitField('Log in')
