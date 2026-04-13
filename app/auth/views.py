from app.auth import auth
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User
from app.extensions import db
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user


@auth.route('/signup', methods=["GET", "POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Process registration logic here
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        # Save user to the database
        try:
           db.session.add(user)
           db.session.commit()
        except Exception as e:
            db.session.rollback()
            # Handling Exception
            print(f"Error occurred while saving user: {e}")
            flash("An error occurred while creating your account. Please try again.", "danger")
            return redirect(url_for('auth.signup'))
        flash("Congratulations, you are now a registered user!", "success")
        return redirect(url_for('auth.login'))
        

    return render_template('auth/signup.html', title='Sign Up', form=form)

@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Process login logic here
        user = User.query.filter_by(email=form.email.data).first()
        try:
            login_user(user, remember=form.remember_me.data)
        except Exception as e:
            print(f"Error occurred during login: {e}")
            flash("An error occurred while logging in. Please try again.", "danger")
            return redirect(url_for('auth.login'))
        flash("Logged in successfully!", "success")
        return redirect(url_for('main.home'))
    return render_template('auth/login.html', title='Login', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('main.home'))