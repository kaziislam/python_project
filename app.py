from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_projects():
    if request.method == 'POST':
        username = request.form['username']
        response = requests.get(f"https://api.github.com/users/{username}/repos")
        my_projects = response.json()
        return render_template('projects.html', projects=my_projects, username=username)
    return render_template('index.html', projects=[])


if __name__ == '__main__':
    app.run(debug=True)
