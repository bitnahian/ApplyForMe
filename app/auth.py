from flask_wtf import Form, FlaskForm
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, InputRequired
from flask import Flask, session, redirect, url_for, escape, request
from settings import *
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = SECRET_KEY
csrf = CSRFProtect(app)

oauth_uri = 'https://accounts.freelancer.com/oauth/authorise'
client_id = 'b0ecd00f-96a4-4391-b260-ce9e86fabbfd' # Need to set this up
client_secret = '79912b13183f232f8be46ed0a5ed4fdcb7d7ac7c1ea6adf5ff95f1efe97524ed791c6c5132edade7bcbeb4b47a1b09297e01dad3b4ecd29cdb123b8eda52bfdb' # Need to set this up too
redirect_uri = '/redirect_endpoint'
prompt = 'select_account consent'
advanced_scopes = '1 2 3 4 5 6'


#LoginForm is inheriting from the Form class
class LoginForm(FlaskForm):
    email = EmailField('Enter your email', validators=[InputRequired('An email is required'), Email(), validators.Length(min=3, max=50)])
    password = PasswordField('Enter your password', validators=[InputRequired('A password is required'), validators.Length(min=4, max=80)])
