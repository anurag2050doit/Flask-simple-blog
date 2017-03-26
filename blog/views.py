from flask_blog import app , db
from flask import render_template, redirect, flash , url_for, abort , session
from blog.models import Blog
from user.models import User
from blog.form import SetupForm
from user.decorator import login_required
import bcrypt

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"

@app.route('/admin')
@login_required
def admin():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    if session.get('is_author'):
        return render_template('blog/admin.html')
    else:
        abort(403)

@app.route('/setup', methods=('GET','POST'))
def setup():
    form = SetupForm()
    error = None
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        user = User(
            form.fullname.data,
            form.email.data,
            form.username.data,
            hashed_password,
            True
        )
        db.session.add(user)
        db.session.flush()
        if user.id:
            blog = Blog(form.name.data, user.id)
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error creating user"
        if user.id and blog.id:
            db.session.commit()
            flash('Blog created')
            return redirect(url_for('admin'))
        else:
            db.session.rollback()
            error = "Error creating blog"
    return   render_template('blog/setup.html', form=form, error=error)
