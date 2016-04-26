import os, sys
from flask import (Flask,
                   request,
                   session,
                   render_template,
                   redirect,
                   url_for,
                   flash)
from functools import wraps
import gfm
import yaml
import hashlib

DEBUG = os.environ.get('DEBUG', False)

app = Flask(__name__)

try:
    JOTIT_ROOT = os.path.join(os.path.dirname(__file__))
    defaults_filename = '%s/defaults.yml' % JOTIT_ROOT
    with open(defaults_filename, 'r') as defaults_yaml:
        DEFAULTS = yaml.load(defaults_yaml.read())
    SETTINGS = DEFAULTS.copy()
    config_filename = './config.yml'
    with open(config_filename, 'r') as config_yaml:
        CONFIG = yaml.load(config_yaml.read())
    SETTINGS.update(CONFIG)
except Exception, e:
    print('Need config, yo.')
    print(e)
    sys.exit(0)

app.secret_key = SETTINGS['secret_key']


class JotIt():


    def login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if SETTINGS['login_required']:
                try:
                    session['username']
                except:
                    return redirect(url_for('login'))
                else:
                    return f(*args, **kwargs)
            else:
                return f(*args, **kwargs)
        return decorated_function


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html', settings=SETTINGS)
        else:
            username = request.form.get('username', None)
            password = request.form.get('password', None)
            if username is not None and username != '' and password is not None and password != '':
                try:
                    user = (user for user in SETTINGS['users'] if user['username'] == username).next()
                except:
                    flash('Invalid username')
                    return redirect(url_for('login'))
                else:
                    password_hash = hashlib.sha512(password).hexdigest()
                    if user['password_hash'] == password_hash:
                        session['username'] = username
                        return redirect(url_for('index'))
                    else:
                        flash('Incorrect password')
                        return redirect(url_for('index'))
            else:
                flash('Missing form data')
                return redirect(url_for('index'))


    @app.route('/logout')
    def logout():
        session.pop('username', None)
        return redirect(url_for('index'))


    @app.route('/')
    @login_required
    def index():
        files = []
        for root, directories, filenames in os.walk('./content/'):
            for filename in filenames:
                full_filename = os.path.join(root, filename)[9:-3]
                files.append(full_filename)
        files = sorted(files)
        return render_template('index.html', files=files, settings=SETTINGS)


    @app.route('/<path:path>')
    @login_required
    def content(path=None):
        if path == '' or path is None:
            path = 'index'
        while path.endswith('/'):
            path = path[:-1]
        filename = './content/%s.md' % path
        try:
            with open(filename, 'r') as file_md:
                file_html = gfm.markdown(file_md.read())
                return render_template('content.html', content=file_html, settings=SETTINGS)
        except IOError, e:
            error_text = '404 Not Found'
            return render_template('error.html', error_text=error_text, settings=SETTINGS)


    def new_jotit(self):
        return app
