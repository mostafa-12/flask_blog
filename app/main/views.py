from app.main import main
from app.models import Post
from flask import render_template, url_for
from flask_login import login_required, current_user

@main.route('/')
@main.route('/home')
def home():
    return render_template('main/home.html', title='Home')


@main.route('/posts')
@login_required
def posts():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('main/posts.html', title='Posts', posts=posts)

@main.route('/profile')
@login_required
def profile():
    return render_template('main/dashboard.html', title= current_user.username + "'s Profile")

