from flask import Flask, render_template, Response, request
import os
import threading
import re
import requests
import json


app = Flask(__name__)

files = []
def find_files():
    global files
    files = []
    print('Crawling files')
    for x in os.listdir('static'):
        if ('.html' in x):
            with open('static/' + x) as file:
                data = file.read()
                match = re.search("(?<=<!--)([\s\S]*?)(?=-->)", data)
                desc = ""
                if (match):
                    desc = match.group(0)
                result = {
                    "name": x,
                    "description": desc
                }
                files.append(result)

find_files()

@app.route('/')
@app.route('/home')
def home():
    find_files()
    return render_template('home.html', page="dashboard", files=files)

@app.route('/new')
def new():
    return render_template('new.html', page="new", title="New Email", files=json.dumps(files))

@app.route('/template/<name>')
def temp(name):
    return render_template('page.html', file=name)
    
@app.route('/publish/', methods=['GET', 'POST'])
def publish():
    # Decode data POSTed from Ajax
    data = urllib.parse.parse_qs(request.data.decode())
    html_str = str(data['html'][0])
    contents = html_str
    print(contents)
    # Check if template contains '__link__'
    match = re.search("(<div).+(__link__).*(div>)", html_str, re.MULTILINE)
    if match:
        # Replace line containing '__link__' with an empty line for GitHub Gist
        print('here')
        contents = html_str.replace(match.group(0), '\n')
        obj = {
            "files": {
                data['title'][0]: {
                    "content": contents
                }
            }
        }
        # Create gist from template using GitHub API
        r = requests.post('https://api.github.com/gists', headers={'Authorization': os.environ['GITHUB_API_TOKEN']}, data=json.dumps(obj))
        r = r.json()
        print(r)
        # Extract link from GitHub API response
        link = r['files'][data['title'][0]]['raw_url']
        # Replace '__link__' with Gist link
        contents = html_str.replace('__link__', "https://htmlpreview.github.io/?" + link)
    # Create file in 'static' folder
    with open('static/'+data['title'][0], 'w+') as file:
        file.write(contents)
    return Response("Created", status=201, mimetype='application/json')

@app.route('/send/', methods=['GET', 'POST'])
def send():
    r = requests.post('https://script.google.com/macros/s/AKfycbxzQ3yUR8NJ47PAgM0rR2dxogpapdon0J7yy7no5w6_m4IcA_bY/exec', data=request.form)
    print(r)
    return Response("Created", status=201, mimetype='application/json')


if __name__ == '__main__':
    print("Spinning up new thread..")
    thread = threading.Thread(target=app.run(debug=True))
    thread.start()