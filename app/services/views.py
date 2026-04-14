from . import services
from app.extensions import db
from app.utilities import save_pic_secure
from .forms import EditProfileForm, PostForm
from app.models import Post
from flask import render_template, flash, request, url_for, redirect
from flask_login import login_required
from flask_login import current_user

@services.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    if form.validate_on_submit():
        user = current_user
        user.username = form.username.data
        user.email = form.email.data
        if form.picture.data:
            picture_file = save_pic_secure(form.picture.data)
            user.profile_picture = picture_file
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
            flash('An error occurred while updating your profile. Please try again.', 'danger')
            return redirect(url_for('services.edit_profile'))
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('main.profile', username=user.username))
    return render_template('services/edit_profile.html', title='Edit Profile', form = form)


@services.route("/create_post", methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title = form.title.data,
            content = form.content.data,
            author = current_user
        )
        cover = save_pic_secure(form.cover_image.data)
        post.cover_image = cover if cover else "default_post.jpg"
        try:
            db.session.add(post)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('An error occurred while saving the post. Please try again.', 'danger')
            return redirect(url_for("services.create_post"))
        flash("Post posted successfully", "success")
        return redirect(url_for("main.profile"))
    return render_template('services/create_post.html', title='Create Post', form=form)

@services.route("/remove_post/<int:post_id>", methods=['POST'])
@login_required
def remove_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author.id != current_user.id:
        flash("You are not authorized to delete this post.", "danger")
        return redirect(url_for("main.profile"))
    try:
        db.session.delete(post)
        db.session.commit()
    except Exception as e:
        print(e)
        flash('An error occurred while deleting the post. Please try again.', 'danger')
        return redirect(url_for("main.profile"))
    flash("Post deleted successfully", "success")
    return redirect(url_for("main.profile"))

@services.route("/edit_post/<int:post_id>", methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if request.method == 'GET':    
        form.title.data = post.title
        form.content.data = post.content
    if post.author.id != current_user.id:
        flash("You are not authorized to edit this post.", "danger")
        return redirect(url_for("main.profile"))
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        if form.cover_image.data:
            cover = save_pic_secure(form.cover_image.data)
            post.cover_image = cover if cover else post.cover_image
        try:
            db.session.add(post)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('An error occurred while updating the post. Please try again.', 'danger')
            return redirect(url_for("services.edit_post", post_id=post.id))
        flash("Post updated successfully", "success")
        return redirect(url_for("main.get_post", post_id=post.id))
    
    return render_template('services/edit_post.html', title='Edit Post', form=form, post=post)
    
