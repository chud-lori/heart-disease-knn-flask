from flask import (render_template, url_for, flash,
                    redirect, request, Blueprint,
                    current_app, make_response, session)
from corpe import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from corpe.models import Admin, Dataset

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # clear session every load this page
    session.clear()
    return render_template('main/index.html', title='LORI')

@main_bp.route('/about')
def about():
    return render_template('main/about.html', title='Tentang')

@main_bp.route('/guide')
def guide():
    return render_template('main/guide.html', title='Petunjuk Penggunaan')

@main_bp.route('/heart')
def heart():
    return render_template('main/heart.html', title='Jantung')
