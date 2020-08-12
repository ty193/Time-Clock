import os

from flask import Flask, render_template, request, flash, redirect, session, g, abort
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from forms import UserAddForm, UserEditForm, LoginForm
from models import db, connect_db, Employee, Time

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgres:///time'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
toolbar = DebugToolbarExtension(app)

connect_db(app)


###################################################################################
# User new userlogin/logout


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = Employee.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(employee):
    """Log in user."""

    session[CURR_USER_KEY] = employee.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If there already is a user with that username: flash message
    and re-present form.
    """
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    form = UserAddForm()

    if form.validate_on_submit():
        try:
            employee = Employee.signup(
                name=form.name.data,
                username=form.username.data,
                password=form.password.data,
                admin=form.admin.data,
            )
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(employee)

        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        employee = Employee.authenticate(form.username.data,
                                         form.password.data)

        if employee:
            do_login(employee)
            flash(f"Hello, {employee.name}!", "success")
            return redirect("/")

        flash("Invalid credentials.", "danger")

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()

    flash("You have successfully logged out.", 'success')
    return redirect("/login")


###################################################################################
# Employee routes

@app.route('/')
def home():
    """Return home page."""

    return render_template('home.html')


@app.route('/time-clock', methods=['POST'])
def time_clock():

    if not g.user:
        flash("Access unuthorized.", "danger")
        return redirect("/")

    

    return render_template('/users/punch.html')


@app.route('/pay-period')
def pay_period():
    """Return a page to select a pay period"""

    return render_template('pay_period.html')


# @app.route("/time")
# def show_employees_hours():


@app.after_request
def add_header(req):
    """Add non-caching headers on every request."""

    req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    req.headers["Pragma"] = "no-cache"
    req.headers["Expires"] = "0"
    req.headers['Cache-Control'] = 'public, max-age=0'
    return req
