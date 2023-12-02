from config import app
from flask import Blueprint, request, render_template, redirect
from flask_login import logout_user, login_required, current_user
from routes.login import first_route
from routes.sign_up import second_route


app.register_blueprint(first_route)
app.register_blueprint(second_route)


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/login")

@app.route("/")
@login_required
def profile():
    return render_template('index.html', name=current_user.username)


@app.route("/zachita")
@login_required
def zachita():
    return render_template('zachita.html', name=current_user.username, pwd = current_user.pwd)



if __name__ == '__main__':
    app.run(debug=True)