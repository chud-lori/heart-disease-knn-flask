from flask import (render_template, url_for, flash, redirect,
                    request, Blueprint, current_app, make_response)
from corpe import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from corpe.models import Admin
from corpe.admin.forms import LoginForm

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.home'))
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin, remember=form.remember.data)
            next = request.args.get('next')
            return redirect(next or url_for('admin.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('admin/login.html', title='Login', form=form)

@admin_bp.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@admin_bp.route('/home')
@login_required
def home():
    return make_response(f'Allo {current_user.username}')

@admin_bp.route('/gen')
def gen():
    """ Endpoint to create admin row"""
    password = bcrypt.generate_password_hash('tidaktau').decode('utf-8')
    admin = Admin(email='lori@email.com', username='Lori', password=password)
    admin_db = Admin.query.filter_by(email=admin.email).first()
    if admin_db:
        return redirect(url_for('admin.login'))
    db.session.add(admin)
    db.session.commit()
    return make_response(f'Hei {admin.username}')