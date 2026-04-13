from matplotlib.pylab import tile

from app.auth import auth
from app.auth.forms import LoginForm, RegistrationForm
from flask import render_template


@auth.route('/signup')
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Process registration logic here
        pass
    return render_template('auth/signup.html', title='Sign Up', form=form)

@auth.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Process login logic here
        pass
    return render_template('auth/login.html', title='Login', form=form)

@auth.route('/logout')
def logout():
    return "Logout Page"