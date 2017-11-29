from flask import Flask, render_template, Markup, request, jsonify
from auth import LoginForm
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index/index.html')

@app.route('/login')
def login():
    header = "user", "password"
    data = "user", "password"
    r = requests.post('https://www.freelancer.com/api/users/0.1/users/check/',
          data={"user": "password"},
          header={'key': 'value'})
    print(r)
    # print(r)
    # form = LoginForm()
    # error = None
    return render_template('auth/login.html')

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

    r = requests.get(url, params=payload)
    root = ET.fromstring(r.content)
    response = {'title' : [], 'description' : [], 'url' : []}
    for listing in root.iter('listing'):
        title = listing.get('title')
        description = listing.get('description')
        url = listing.find('company').get('url')
        #print(' * {} {}'.format(
        #    title, description
        #    ))
        #print('\n\n')
        response['title'].append(title)
        response['description'].append(description)
        response['url'].append(url)
    return jsonify(response)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
