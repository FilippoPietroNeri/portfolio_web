import requests
from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    repos = requests.get('https://api.github.com/users/FilippoPietroNeri/repos')
    outputRepo = []
    for repo in repos.json():
        if 'project' in repo['topics']:
            outputRepo.append(repo)
    return render_template('index.html', projects=outputRepo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)