from flask_blog import app
from user.form import ResgisterForm, LoginForm
from flask import render_template, redirect, session
from user.models import User
@app.route('/login', methods=('GET','POST'))
def login():
    form = LoginForm()
    error = None

    if form.validate_on_submit():
        user = User.query.filter_by(
            username = form.username.data,
            password = form.password.data
        ).limit(1)
        if user.count():
            session['username'] = form.username.data
            return redirect('/login_success')
        else:
            error = 'Incorrect Username and Password'
    return render_template('user/login.html', form=form, error=error)

@app.route('/login_success')
def login_success():
    return 'Author Login in'

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = ResgisterForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('user/register.html', form=form)

@app.route("/success")
def success():
    return "Welcome"
