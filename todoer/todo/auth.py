import functools

from flask import (
    Blueprint, flash, g, render_template, request, url_for, sesions
         )

from werkzeug.secuity import check_password_hash, generatepassword_hash

from todo.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET','POST'])
def rgister():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, c = get_db()
        error = None
        c.execute(
            "select id from user mhere username = %d"
        )
