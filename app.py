from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to my simple blog!'


@app.route('/api/blog/categories')
def categories():
    return 'This is the category section!'


@app.route('/api/blog/search')
def search(name="Devops"):
    name = request.args.get('name', name)
    return "{} not found!".format(name)
