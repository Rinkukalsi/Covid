from flask import Blueprint, render_template
from flask_login import login_required, current_user



views = Blueprint("views", __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html")


@views.route('/grocerry')
def grocerry():
    return render_template("Grocery.html")

@views.route('/meds')
def medecine():
    return render_template("meds.html")

@views.route('/help-line')
def helpline():
    return render_template("helpline.html")