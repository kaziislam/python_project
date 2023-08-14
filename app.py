from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def get_projects():
    response = requests.get("https://api.github.com/users/kaziislam/repos")
    my_projects = response.json()
    return render_template('projects.html', projects=my_projects)


if __name__ == '__main__':
    app.run(debug=True)
