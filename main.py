from flask import Flask
from flask_login import UserMixin
from config import app
import hashlib
from config import db
from flask_wtf import FlaskForm




class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def get_id(self):
        return self.id



class register_form(FlaskForm):
    username = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    pwd = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')



class login_form(FlaskForm):
    email = StringField(validators=[DataRequired()])
    pwd = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Войти')



@app.route("/")
def all_name():
    try:

        return  render_template('index.html')
    except Exception as e:
        error_body = {'reason': 'Unknown error'}
        return  render_template('index.html')


@app.route("/", methods=("GET", "POST"))
def index():
    return render_template("index.html",title="Home")


@app.route("/login")
def login():
    form = login_form()
    return render_template("login.html",form=form)



@app.route("/login", methods=("POST"))
def register():
    form = register_form()
    return render_template("login.html",form=form)


@app.route("/signup")
def signup():
    form = register_form()
    return render_template("signup.html",form=form)

@app.route("/signup", methods=("POST"))
def signup_1():
    form = register_form()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        pwd = form.pwd.data
        valid_email = list(map(lambda x: x.get_id(), User.query.filter_by(email=email)))
        if valid_email is None:
            pwd = pwd.hexdigest() #хэширование
            new_user = User(username, email, pwd)
            db.session.add(new_user)
            db.session.commit()
            return render_template("login.html", form=form)
        error_body = {'reason': 'This email already exist'}
        return render_template('signup.html', res=error_body, form=form)
    error_body = {'reason': 'Form is not validate'}
    return render_template('signup.html', res=error_body, form=form)




@app.route("/logout")
def logout():
    return render_template("signup.html", form=form)




if __name__ == '__main__':
    app.run(debug=True)