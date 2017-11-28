from flask import Flask, render_template
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def home():
    payload = {'api_key' : 'e13265054e9ac26df0699a76972404b7', 'method' : 'aj.jobs.search', 'perpage' : '10'}
    payload['keywords'] = 'python,java'

    url='https://authenticjobs.com/api/'

    r = requests.get(url, params=payload)
    root = ET.fromstring(r.content)
    response = ''

    for listing in root.iter('listing'):
        title = listing.get('title')
        description = listing.get('description')
        #print(' * {} {}'.format(
        #    title, description
        #    ))
        #print('\n\n')
        response += title + description

    return response


@app.route('/about')
def about():
    return rete('about.html')

if __name__ == '__main__':
    app.run(debug=True)
