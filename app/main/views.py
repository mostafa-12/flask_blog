from app.main import main
from flask import render_template, url_for

@main.route('/')
@main.route('/home')
def home():
    return render_template('main/home.html', title='Home')


@main.route('/posts')
def posts():
    return 

@main.route('/profile')
def profile():
    return 

