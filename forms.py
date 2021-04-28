from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])


class RegistrationForm(FlaskForm):
    email = StringField('email', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])


class BlogPost(FlaskForm):
    title = StringField('title', validators=[InputRequired()])
    content = TextAreaField('password', validators=[InputRequired()],)


class AddCommentForm(FlaskForm):
    comment_content = StringField('comment_content', validators=[InputRequired()])
    submit = SubmitField("Posted")


