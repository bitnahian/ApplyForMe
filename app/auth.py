from flask_wtf import Form, FlaskForm
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, InputRequired

#LoginForm is inheriting from the Form class
class LoginForm(FlaskForm):
    email = EmailField('Enter your email', validators=[InputRequired('An email is required'), Email(), validators.Length(min=3, max=50)])
    password = PasswordField('Enter your password', validators=[InputRequired('A password is required'), validators.Length(min=4, max=80)]) 
