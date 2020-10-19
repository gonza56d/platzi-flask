from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest

from app import create_app
from app.forms import LoginForm


app = create_app()

todos = ['TODO 1', 'TODO 2']


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
def hello():
    user_ip = session.get('user_ip')
    username = session.get('username')
    context = {'user_ip': user_ip, 'todos': todos, 'username': username}

    return render_template('hello.html', **context)
