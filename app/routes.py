from flask import render_template, flash, redirect, url_for

from app import app

from .forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            'Login requested for user: {}; Remember Me option: {}'.format(form.username.data, form.remember_me.data)
        )
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
