from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app.models.user import User

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        user = User.query.filter_by(email=email).first()

        if user and user.check_senha(senha):
            login_user(user)
            return redirect(url_for('auth.dashboard'))
        flash('Email ou senha inválidos')

    return render_template('login.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    return "Área logada"

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))