from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, length
from flask_wtf import FlaskForm


class SignupForm(FlaskForm): #Inheriting this enables us to work with SECRET_KEY
    username = StringField("UserName", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_pass = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired(), length(max=500)])
    submit = SubmitField("Submit")

