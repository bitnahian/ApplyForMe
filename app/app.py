from flask import Flask, render_template, Markup, request, jsonify
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/process')
def process():
    print("HERE")
    # Construct API params
    payload = {'api_key' : 'e13265054e9ac26df0699a76972404b7', 'method' : 'aj.jobs.search', 'perpage' : '10'}
    # Receive keywords from jQuery script
    keywords = request.args.get('keywords', 0, type=str)
    if keywords is None:
        return jsonify({"error" : "Keywords not specified"})

    keywords.replace(" ", "")
    payload['keywords'] = keywords

    url='https://authenticjobs.com/api/'

    r = requests.get(url, params=payload)
    root = ET.fromstring(r.content)
    response = {'title' : [], 'description' : []}
    for listing in root.iter('listing'):
        title = listing.get('title')
        description = listing.get('description')
        #print(' * {} {}'.format(
        #    title, description
        #    ))
        #print('\n\n')
        response['title'].append(title)
        response['description'].append(description)

    return jsonify(response)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
