from app.main import main
from app.main.forms import CommentForm
from app.models import Post, Comment
from app.extensions import db
from flask import render_template, url_for, redirect
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
    comments = current_user.comments.order_by(Comment.timestamp.desc()).all()
    return render_template('main/dashboard.html', title= current_user.username + "'s Profile", comments=comments)

@main.route('/post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = post.comments.order_by(Comment.timestamp.desc()).all()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = Comment(content=comment_form.content.data, author=current_user, post=post)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.get_post', post_id=post.id))
    return render_template('main/post_detail.html', title=post.title, post=post, comments=comments, comment_form=comment_form)