from flask_login import UserMixin
from config import app
from config import db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask import Blueprint, request, render_template, redirect
from flask_login import logout_user


from routes.login import first_route
from routes.sign_up import second_route


app.register_blueprint(first_route)
app.register_blueprint(second_route)


@app.route('/logout', methods=(["POST"]))
def logout():
    logout_user()
    return redirect("/login")

@app.route("/")
def all_name():
        return render_template('index.html')


@app.route("/", methods=(["POST"]))
def index():
    return render_template("index.html",title="Home")





if __name__ == '__main__':
    app.run(debug=True)