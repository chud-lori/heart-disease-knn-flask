"""
Main routes for main site view
"""

from flask import (render_template, Blueprint, session)

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """
        Route for index in /
        clear session every load this page to remove id session
    """
    session.clear()
    return render_template('main/index.html', title='LORI')


@main_bp.route('/about')
def about():
    """
    about page
    """
    return render_template('main/about.html', title='Tentang')


@main_bp.route('/guide')
def guide():
    """
    guide page
    """
    return render_template('main/guide.html', title='Petunjuk Penggunaan')


@main_bp.route('/heart')
def heart():
    """
    heart dissease inforamtion page
    """
    return render_template('main/heart.html', title='Jantung')
