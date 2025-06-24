from flask import (request, render_template, redirect, url_for, Blueprint, flash, abort)
from flask_login import (login_user,logout_user, login_required, current_user)
from werkzeug.security import check_password_hash, generate_password_hash
from auth.forms import LoginForm, RegisterForm
from models import db, User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("home"))
        flash("Invalid Credentials")
    return render_template("auth/login.html", form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if not current_user.is_admin:
        abort(403)

    form = RegisterForm()
    if form.validate_on_submit():
        existente = User.query.filter_by(username=form.username.data).first()
        if existente:
            flash("Este usuario ya existe", "warning")
            return redirect(url_for('auth.register'))
        
        nuevo = User(
            username=form.username.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(nuevo)
        db.session.commit()
        flash("Usuario creado exitosamente", "success")
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', form=form)


@auth_bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('landpage'))