from flask_wtf import Form, FlaskForm
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, InputRequired
from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = 'rastanns'

sessions = {}

#LoginForm is inheriting from the Form class
class LoginForm(FlaskForm):
    email = EmailField('Enter your email', validators=[InputRequired('An email is required'), Email(), validators.Length(min=3, max=50)])
    password = PasswordField('Enter your password', validators=[InputRequired('A password is required'), validators.Length(min=4, max=80)]) 

@app.route('/')
def index():
    return render_template('index/index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        session['username'] = { 'email' : email , 'cart' : [0] }
        return redirect('form/form.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('index/index.html')
        
