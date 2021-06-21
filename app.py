from flask import Flask

from flask import render_template
app = Flask(__name__)


posts = [
    {
        'title': 'Devops and Cloud Native',
        'author': 'Dare',
        'day': 'day one',
        'content': 'Onboarding and installing applications in lesson one',
        'date_posted': 'June 15, 2021'
    },
    {
        'title': 'Devops and Cloud Native',
        'author': 'Fredrick',
        'day': 'day two',
        'content': 'Implementing Lesson One',
        'date_posted': 'June 16, 2021'
    },
    {
        'title': 'Devops and Cloud Native',
        'author': 'Kelly',
        'day': 'day three',
        'content': 'Working on Demo and implementing Lesson two',
        'date_posted': 'June 17, 2021'
    },
    {
        'title': 'Devops and Cloud Native',
        'author': 'Achiever',
        'day': 'day four',
        'content': 'Revising lesson two and improving flask project',
        'date_posted': 'June 18, 2021'
    }


]


@app.route('/')
@app.route('/home')
def home():
    return 'Welcome to my simple blog!'


@app.route('/about')
def about():
    return 'About Page!'


@app.route('/api/blog/categories')
def categories():
    return 'This is the category section!'


@app.route('/api/blog/daily')
def daily():
    return render_template('index.html', posts=posts)


# if __name__ == "__main__":
#     app.run(debug=True, port=9000, host='0.0.0.0')
