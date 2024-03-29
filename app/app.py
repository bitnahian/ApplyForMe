from flask import Flask, render_template, Markup, request, jsonify, flash, redirect, url_for, json, make_response
from auth import *
import requests
import xml.etree.ElementTree as ET
from flask_wtf.csrf import CSRFProtect


@app.route('/index')
@app.route('/')
def home():
    return render_template('index/index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if 'username' in session and session['username'] is not None:
        form = LoginForm(request.form)
        if request.method == 'POST':
            if form.validate() == False:
                flash('All fields are required.')
                return render_template('auth/login.html', form=form)
            else:
                title = request.form['title']
                description = request.form['description']
                link = request.form['link']
                budget = request.form['budget']
                job_ids = get_job_id()
                url = "https://www.freelancer-sandbox.com/api/projects/0.1/projects/"
                oauth_headers = {"freelancer-oauth-V1": "k00e8P5saxuzfkoHcJOcMhT0pJcgt9",  "Content-Type" : "application/json"}
                data = {
                "title": title,
                "description": description + "Application Link: " + link,
                "currency": {
                    "code": "AUD",
                    "id": 3,
                    "sign": "$"
                    },
                "budget": {
                        "minimum": budget
                    },
                "jobs": job_ids
                }
                resp = requests.post(url, headers=oauth_headers, data=json.dumps(data))
                response = json.loads(resp.text)
                print(jsonify(response))

                return render_template('index/index.html')
        elif request.method == 'GET':
            return render_template('auth/login.html', form=form)
    else:
        return redirect(url_for('handle_authorize'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/form')
def form():
    if 'username' in session and session['username'] is not None:
        return render_template('form/form.html')
    else:
        return redirect(url_for('handle_authorize'))

@app.route('/add_cart', methods=['GET'])
def get_cart():
    cartID = request.args.get('cartID', 0, type=str) #Get jobsb ID from Javascript
    title = request.args.get('title', 0, type=str) #Get jobsb ID from Javascript
    description = request.args.get('description', 0, type=str) #Get jobsb ID from Javascript


    if int(cartID) != -100: #Add new cart item

        session['cart']['id'].append(cartID)
        session['cart']['title'].append(title)
        session['cart']['description'].append(description)
        session.modified = True

    counter = 0

    response = {'title' : [], 'description' : []}

    for x in session['cart']['title']:
        response['title'].append(x)
        response['description'].append(session['cart']['description'][counter])
        counter+=1
    return jsonify(response)


@app.route('/remove_cart', methods=['GET'])
def remove_cart():
    cartID = request.args.get('cartID', 0, type=str) #Get jobsb ID from Javascript
    # for x in range (0, session['username'].length):
    #     if (session['username']['cart']['id'] == cartID):
    #         #remove

    session['cart']['title'].append(title)
    session['cart']['description'].append(description)
    session.modified = True

    counter = 0
    response = {'title' : [], 'description' : []} #TODO add link
    for x in session['cart']['title']:
        response['title'].append(x)
        response['description'].append(session['cart']['description'][counter])
        counter+=1
    return jsonify(response)


@app.route('/confirmation')
def confirmation():
    return render_template('confirmation/confirmation.html' )

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

# Users who hit this endpoint will be redirected to the authorisation prompt
@app.route('/authorize')
def handle_authorize():
    return redirect(
        '{0}?response_type=code'
        '&client_id={1}&redirect_uri={2}'
        '&scope=basic&prompt={3}'
        '&advanced_scopes={4}'.format(
            oauth_uri, client_id, redirect_uri, prompt, advanced_scopes
        )
    )

# The endpoint waiting to receive the authorisation grant code
@app.route('/redirect_endpoint')
def handle_redirect():
#    if 'code' in request.args == True:
    authorisation_code = request.args['code']
    url = "https://www.freelancer-sandbox.com/api/users/0.1/self/"
    oauth_headers = {"Freelancer-OAuth-V1": "k00e8P5saxuzfkoHcJOcMhT0pJcgt9", "display_info" : "True"}
    resp = requests.get(url, headers=oauth_headers)
    response = json.loads(resp.text)

    if response['status'] == "success":
        username = response['result']['username']
        session['username'] = { 'auth' : "k00e8P5saxuzfkoHcJOcMhT0pJcgt9" , 'username' : username }
        session['cart'] = {'id': [], 'title': [], 'description': []}
        return render_template('form/form.html')
    else:
        flash("Authorization unsuccessful. Please authorize with correct information.")
        return redirect(url_for('handle_authorize'))

@app.route('/about')
def about():
    return render_template('about/about.html')

@app.route('/submit_jobs')
def submit_jobs():
    # Get the params
    titles = ["Fix Nahian 1", "Fix Shenin 2", "Fix Ali 3"]
    descriptions = ["test pls", "test pls", "test pls"]
    job_ids = get_job_id()
    budgets = json.loads(request.args.get('budgets'))
    print(budgets)
    url = "https://www.freelancer-sandbox.com/api/projects/0.1/projects/"
    oauth_headers = {"freelancer-oauth-V1": "k00e8P5saxuzfkoHcJOcMhT0pJcgt9",  "Content-Type" : "application/json"}

    budget_len = len(budgets)
    for i in range (0, budget_len):
        if budgets[i] == -1:
            continue
        # Else do the API call
        title = session['cart']['title'][i]
        description = session['cart']['description'][i]
        id = session['cart']['cartID'][i]

        description += "   Apply Here: https://authenticjobs.com/jobs/" + id
        data = {
        "title": titles[i],
        "description": descriptions[i],
        "currency": {
            "code": "AUD",
            "id": 3,
            "sign": "$"
            },
        "budget": {
                "minimum": budgets[i]
            },
        "jobs": job_ids
        }
        resp = requests.post(url, headers=oauth_headers, data=json.dumps(data))
        response = json.loads(resp.text)
        print(jsonify(response))

    # REMEMBER TO POP CART SESSION
    data = json.dumps({"status" : "success", "message":"Application was successful."})
    session.pop('user', None)
    session.pop('cart', None)
    return data

if __name__ == '__main__':
    app.run(debug=True)

def get_job_id():
    url = "https://www.freelancer-sandbox.com/api/projects/0.1/jobs"
    oauth_headers = {"freelancer-oauth-V1": "k00e8P5saxuzfkoHcJOcMhT0pJcgt9",  "Content-Type" : "application/json"}
    job_names = ["resumes" , "communications", "writing", "proofreading", "speechwriting"]
    payload = {"job_names[]" : job_names}
    resp = requests.get(url, headers=oauth_headers, params=payload)
    response = json.loads(resp.text)
    job_ids = []
    for item in response['result']:
        job_ids.append({'id' : item['id']})
    return job_ids
