from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Anton'}
    posts = [
        {
            'author': {'username': 'Tania'},
            'body': 'I like gelatto!'
        },
        {
            'author': {'username': 'Masha'},
            'body': 'I like playing dols.'
        },
        {
            'author': {'username': 'Vitia'},
            'body': 'I like tools.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
