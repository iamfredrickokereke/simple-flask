from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to my simple blog!'


@app.route('/api/blog/categories')
def categories():
    return 'This is the category section!'
