from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.forms import LoginForm
from app.models.tables import User 


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])

def login():
    form =  LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("index"))
            flash('Logged in.')
        else:
            flash('Invalid login.')
    else:
        print(form.errors)
    return render_template('login.html',form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))
