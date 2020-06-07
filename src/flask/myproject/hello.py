from flask import Flask, url_for, request, render_template
from markupsafe import escape
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User { escape(username)}'

@app.route('/port/<int:post_id>')
def show_post(post_id):
    return f'Post { post_id }'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath { escape(subpath) }'

@app.route('/about')
def about():
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Posted'
    else:
        return 'Got'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))


@app.route('/params')
def params():
    username = request.cookies.get('username')
    username = request.args.get('key', '')
    passwrod = request.form['password']

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('show_user_profile', username='atul sharma'))
    print(url_for('about', next='/'))
    print(url_for('static', filename='style.css'))

