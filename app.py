from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    search = request.args.get('search')
    video = request.args.get('video')
    if not search:
        return render_template('index.html')
    if not video:
        return 'hasil search adalah ' + search
        
    return 'hasil search adalah ' + search + ' video nya adalah ' + video

@app.route('/setting')
def show_setting():
    return 'ini adalah halaman setting'

@app.route('/profile/<username>')
def show_profile(username):
    return render_template('profile.html', username=username)

@app.route('/blog/<int:blog_id>')
def show_blog(blog_id):
    return 'ini adlaah halaman blog %s' % blog_id

@app.route('/login', methods=['GET', 'POST'])
def show_login():
    if request.method == 'POST':
        return 'Email adalah : ' + request.form['email']

    return render_template('login.html')    