from flask import request, make_response, redirect, render_template, session
from flask_login import login_required
import unittest

from app import create_app
from app.firestore_service import get_todos


app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def handle_404(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def handle_500(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    session['user_ip'] = user_ip
    response = make_response(redirect('/hello'))
    return response


@app.route('/hello')
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = session.get('username')
    context = {'user_ip': user_ip, 'todos': get_todos(user_id=username), 'username': username}
    return render_template('hello.html', **context)
