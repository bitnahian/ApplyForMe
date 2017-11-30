from flask import Flask, render_template, Markup, request, jsonify
from auth import *
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index/index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        email = request.form['email']
        session['username'] = { 'email' : email , 'cart' : [0] }
        print(email)
        return redirect('form/form.html')
    return render_template('auth/login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('index/index.html')

@app.route('/form')
def form():
    return render_template('form/form.html')

@app.route('/process')
def process():
    # Construct API params
    payload = {'api_key' : 'e13265054e9ac26df0699a76972404b7', 'method' : 'aj.jobs.search', 'perpage' : '4'}
    # Receive keywords from jQuery script
    keywords = request.args.get('keywords', 0, type=str)
    page = request.args.get('page', 1, type=int)
    if keywords is None:
        return jsonify({"error" : "Keywords not specified"})

    keywords.replace(" ", "")
    payload['keywords'] = keywords
    payload['page'] = page
    url='https://authenticjobs.com/api/'
    # Send request to API
    r = requests.get(url, params=payload)
    # Get the root using Element Tree
    root = ET.fromstring(r.content)
    # Response variable for storing desired output
    response = {'title' : [], 'description' : [], 'id' : [], 'name': [], 'url' : []}
    for listing in root.iter('listing'):
        job_id = listing.get('id')
        title = listing.get('title')
        description = listing.get('description')
        company = listing.find('company')
        url = company.get('url')
        name = company.get('name')
        response['title'].append(title)
        response['description'].append(description)
        response['url'].append(url)
        response['name'].append(name)
        response['id'].append(job_id)

    return jsonify(response)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
