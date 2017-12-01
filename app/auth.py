from flask_wtf import Form, FlaskForm
from wtforms import validators, StringField, PasswordField, TextField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, InputRequired
from flask import Flask, session, redirect, url_for, escape, request
from settings import *
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = SECRET_KEY
csrf = CSRFProtect(app)

oauth_uri = 'https://accounts.freelancer-sandbox.com/oauth/authorise'
client_id = '96ae59dd-a8dd-49af-919b-167a6327a902'
client_secret = '1140823b3e4289a9e0b5cd6c76e63e9d0575b8753448aa99f80e3aad43009e1bfd911f07953041ff83d9a6b4cc845b8d18eece3f2f0e47e78bc187d06abd39f8'
redirect_uri = 'http://localhost:5000/redirect_endpoint'
prompt = 'select_account consent'
advanced_scopes = '1 2 3 4 5 6'


#LoginForm is inheriting from the Form class
class LoginForm(FlaskForm):
    title = TextField('Title', validators=[InputRequired('Title Required'), validators.Length(min=5, max=50)])
    description = TextField('Description', validators=[InputRequired('Description Required'), validators.Length(min=5, max=80)])
    link = TextField('Link', validators=[InputRequired('Link for Application Portal'), validators.Length(min=3, max=150)])
