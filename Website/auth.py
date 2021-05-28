
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint("auth", __name__)

@auth.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        Adhar_number = request.form.get("Adhar_Number")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.Adhar, Adhar_number):
                flash("Logged in", category = 'success')
                login_user(user, remember=True)
            else:
                flash("inncorecct password", category="error")
        else:
            flash("Email does not exist", category='error')
        return redirect(url_for('views.home'))

    return render_template('login.html' ,user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        adhar1 = request.form.get("Adhar_Number1")
        adhar2 = request.form.get("Adhar_Number2")
        user = User.query.filter_by(email=email).first()

        if user:
            flash("user alredy exist", category='error')
        elif len(email) < 7:
            flash("Enter a valid email", category="error")
        elif len(first_name) < 2:
            flash("Enter a valid Name", category="error")
        elif adhar1 != adhar2:
            flash("Pass don\'t match", category="error")
        elif len(adhar1) != 12:
            flash("Enter a valid adhar no.", category="error")
        else:
            new_user = User(email=email, first_name=first_name, Adhar=generate_password_hash(adhar1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created", category="Success")
            return redirect(url_for('views.home'))
          




    return render_template('signup.html',user=current_user)