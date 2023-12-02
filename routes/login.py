from flask import Blueprint, request, render_template, redirect
from config import app
import hashlib
from routes.sign_up import register_form, login_form, Users
from flask_login import login_user

first_route = Blueprint('first_route', __name__)

a = []


@app.route("/login")
def login():
    form = login_form()
    return render_template("login.html",form=form)


@app.route("/login", methods=(["POST"]))
def register():
    form = login_form()
    if form.validate_on_submit():
        email = form.email.data
        pwd = form.pwd.data
        valid_email = list(map(lambda x: x.get_pass(), Users.query.filter_by(email=email)))
        print(valid_email)
        if valid_email:
            pwd = hashlib.sha1(pwd.encode()).hexdigest()
            print(valid_email)
            if pwd == valid_email[0]:
                remember = True if request.form.get('remember') else False
                user = Users.query.filter_by(email=email).first()
                login_user(user, remember=remember)
                return redirect("/")
            error_body = {'reason': 'Try a different password'}
            return render_template("login.html",res=error_body, form=form)
        error_body = {'reason': 'This email not exist'}
        return render_template('signup.html', res=error_body, form=form)
    error_body = {'reason': 'Form is not validate'}
    return render_template("login.html",res=error_body, form=form)