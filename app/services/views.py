from . import services
from app.extensions import db
from app.utilities import save_pic_secure
from .forms import EditProfileForm
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


