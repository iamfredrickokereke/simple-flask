from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to my simple blog!'


@app.route('/about')
def about():
    return 'About Page!'


@app.route('/api/blog/categories')
def categories():
    return 'This is the category section!'


# @app.route('/api/blog/search')
# def search(name="Devops"):
#     name = request.args.get('name', name)
#     return "{} not found!".format(name)


@app.route('/api/blog/day1')
def dayone():
    return render_template('index.html', name='fred')


# if __name__ == "__main__":
#     app.run(debug=True, port=9000)
