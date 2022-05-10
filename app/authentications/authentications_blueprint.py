from flask import Blueprint, request, render_template, redirect, session
from app.db.models import User
from app import db
import logging

authentications_blueprints = Blueprint('authentications_blueprints', __name__)
LOG = logging.getLogger(__name__)


@authentications_blueprints.route('/signin')
@authentications_blueprints.route('/signin', methods=['POST', 'GET'])
def signin():
    LOG.info('Sign In route has been called')
    if 'user' in session:
        return redirect('/')
    if request.method == 'POST':
        username = request.form.get('your_name')
        password = request.form.get('your_pass')
        if username and password is not None:
            user = User.query.filter_by(email=username).first()
            if user:
                if user.password == password:
                    session['user'] = username
                    return redirect('/')

    return render_template('signin.html')


"""
    This route is for Signup to create new account
"""


@authentications_blueprints.route('/signup')
@authentications_blueprints.route('/signup', methods=['POST', 'GET'])
def signup():
    LOG.info('Sign Up route has been called')
    if 'user' in session:
        return redirect('/')
    if request.method == 'POST':
        username = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('pass')
        if username and password is not None:
            entry = User(username=username, email=email, password=password)
            db.session.add(entry)
            db.session.commit()
            return redirect('/signin')

    return render_template('signup.html')


@authentications_blueprints.route('/logout')
def logout():
    LOG.info('Logout route has been called')
    if 'user' in session is not None:
        session.pop('user')
    return redirect('/signin')
